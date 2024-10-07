import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import duckdb
import logging

def update_student_exams_record():
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Define the scope for Google Sheets API
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("/usr/local/airflow/secret.json", scope)

        # Authorize the client
        logging.info("Authorizing Google Sheets client...")
        client = gspread.authorize(creds)

        # Open the Google Sheet 'Student subject analysis'
        logging.info("Opening Google Sheet 'Student subject analysis'...")
        workbook = client.open("Student subject analysis ")
        sheet = workbook.sheet1  # Assuming you're working with the first sheet

        # Fetch only the data range A1:Z41 from the 'Student subject analysis' sheet
        logging.info("Fetching data range A1:AG41 from the Google Sheet...")
        range_data = sheet.get('A1:AG41')  # Fetch the specified range

        # Convert the data into a pandas DataFrame
        df_new = pd.DataFrame(range_data[1:], columns=range_data[0])  # First row as header, rest as data
        logging.info(f"Data fetched and converted to DataFrame: {len(df_new)} rows, {len(df_new.columns)} columns")

        # Step 1: Connect to DuckDB and MotherDuck
        logging.info("Connecting to DuckDB and MotherDuck...")
        con = duckdb.connect("md:")  # MotherDuck connection

        # Check if the 'Student_Exams_record_clean' table already exists
        logging.info("Checking if 'Student_Exams_record_clean' table exists...")
        table_exists = con.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'Student_Exams_record_clean'").fetchone()[0]

        # Step 2: Fetch existing data
        existing_df = con.execute("SELECT * FROM Student_Exams_record_clean").fetchdf() if table_exists else pd.DataFrame()

        # Step 3: Compare Google Sheet data with database data to detect changes
        if not existing_df.empty:
            logging.info("Comparing existing data with the Google Sheet data to detect changes...")

            # Check for new or updated rows
            new_or_updated_rows = df_new[~df_new.apply(tuple, 1).isin(existing_df.apply(tuple, 1))]

            if not new_or_updated_rows.empty:
                logging.info(f"Detected {len(new_or_updated_rows)} new or updated rows in the Google Sheet.")

                # Drop existing table and re-create it (optional)
                con.execute("DROP TABLE IF EXISTS Student_Exams_record_clean;")
                logging.info("Old table dropped. Re-creating 'Student_Exams_record_clean' table with updated data...")

                create_sql = create_table_sql("Student_Exams_record_clean", df_new)
                con.execute(create_sql)

                # Insert all data
                placeholders = ', '.join(['?' for _ in df_new.columns])
                insert_sql = f"INSERT INTO Student_Exams_record_clean VALUES ({placeholders})"

                for i, row in df_new.iterrows():
                    con.execute(insert_sql, tuple(row))  # Insert each row

                logging.info(f"All data (including updated rows) successfully inserted into 'Student_Exams_record_clean'.")
            else:
                logging.info("No changes detected in the Google Sheet. Table remains unchanged.")
        else:
            logging.info("No existing data in the database. Inserting all rows from Google Sheet.")

            # Insert all data
            placeholders = ', '.join(['?' for _ in df_new.columns])
            insert_sql = f"INSERT INTO Student_Exams_record_clean VALUES ({placeholders})"

            for i, row in df_new.iterrows():
                con.execute(insert_sql, tuple(row))

            logging.info("All rows successfully inserted into 'Student_Exams_record_clean'.")

        # Close the connection
        con.close()
        logging.info("Closed DuckDB and MotherDuck connections.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise e
