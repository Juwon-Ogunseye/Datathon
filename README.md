# **Prediction Hackathon Project**

This project is developed for the Prediction Hackathon competition, where we are tasked with analyzing student performance data and related metadata to draw meaningful insights about their academic progress. The goal is to develop a solution that tracks and evaluates the academic performance of students, with integration for parental involvement and teacher feedback, using various tools and frameworks.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Data Collection](#data-collection)
3. [Tools and Libraries Used](#tools-and-libraries-used)
4. [Database Architecture](#database-architecture)
5. [Airflow DAGs](#airflow-dags)
6. [Data Flow](#data-flow)
7. [How to Run the Project](#how-to-run-the-project)

---

## **Project Overview**

This project focuses on analyzing student examination data and metadata like parental involvement and teacher feedback. The data is used to predict the potential success of students and how external factors such as parental sentiment (derived from WhatsApp group chats) and teacher assessments affect their academic performance.

We use Google Sheets to store data related to students, teachers, and exams. This data is then processed using Airflow, Google Sheets API, DuckDB, and MotherDuck for storage and analytics. Finally, we evaluate and predict insights from this data using various machine learning techniques, while also capturing how parental and teacher input correlates to student success.

### **Data Source**

The data used in this research was obtained from **Government Secondary School Manchok, Kaura LGA, Kaduna State, Nigeria**. The dataset contains academic records for students in **JSS3 (Junior Secondary School, Grade 9)**, covering one term of academic performance, specifically the third term. 

For privacy reasons, some of the students' names have been changed in this project. We adhered to strict confidentiality rules to protect the identities of the students involved in this study.

### **Methodology**

We employed several methodologies in this project:

1. **Research Method**: We conducted research to understand the educational system and parental involvement dynamics to guide our data collection and analysis.
2. **Data Mining**: Applied to derive insights from the available data and identify patterns in student performance.
3. **Data Engineering**: Focused on cleaning and transforming the data for further analysis.

---

## **Data Collection**

The main sources of data are:

- **Student Performance Data**: Contains the students' exam scores across different subjects, including Math, English, Science, etc. This data is fetched from a Google Sheet.
- **Parental Involvement Data**: Contains text from the school's WhatsApp group, where parents provide feedback, ask questions, or interact with teachers. Sentiment analysis is applied to this data to gauge parental involvement.
- **Teacher Feedback**: Data collected from teachers about student behavior and overall assessment throughout the term. This data is also stored in a Google Sheet.

We use **Google Sheets API** to pull this data into our system for further processing.

---

## **Tools and Libraries Used**

### **Data Collection**
- **Google Sheets API**: Used to fetch real-time data from the Google Sheets where the student, teacher, and parental involvement data is stored.
- **gspread**: A Python library that provides access to Google Sheets.
- **oauth2client**: A library used for OAuth 2.0 authentication.

### **Data Processing and Storage**
- **DuckDB**: Used for handling local queries and data storage.
- **MotherDuck**: Used for remote storage and querying large datasets, providing more scalability.
- **Pandas**: For efficient data manipulation and transformation.

### **Data Orchestration**
- **Apache Airflow**: For automating workflows, including fetching data from Google Sheets, transforming it, and pushing it to DuckDB and MotherDuck.

### **Deployment and Version Control**
- **Docker**: Used to containerize the application and ensure consistent runtime across different environments.
- **Git**: For version control of the project.

### **Libraries for Machine Learning and NLP**
- **NLTK (Natural Language Toolkit)**: Used for performing sentiment analysis on the parental chat data.
- **scikit-learn**: For training models to predict student success based on the data collected.

---

## **Database Architecture**

The data collected is stored in both **DuckDB** for local processing and **MotherDuck** for more scalable, cloud-based storage. The tables include:

- `Student_Exams_Record`: Contains student exam scores across multiple subjects.
- `Student_Profile`: Contains student demographic information.
- `Teacher_Data`: Includes data about teacher assessments of student behavior and performance.
- `Parent_Sentiment`: Contains analyzed data from WhatsApp group chats, including sentiment scores for each parent's involvement.

---

## **Airflow DAGs**

The following are the three main Airflow DAGs used in the project:

1. **Check MotherDuck Token**:
   - Ensures that the MotherDuck token is available in the environment.

2. **Update Student Exams Record**:
   - Fetches updated student exam data from Google Sheets.
   - Compares it with the existing records in DuckDB/MotherDuck.
   - Updates the data in the database if new data is found.

3. **Update Teacher Data & Student Profiles**:
   - Fetches new student and teacher data from Google Sheets.
   - Updates the `Student_Profile` and `Teacher_Data` tables if new data is found.

---

## **Data Flow**

The following steps describe the overall data flow of the project:

1. **Google Sheets**: The data is stored in multiple Google Sheets (one for exam scores, one for student profiles, one for teacher feedback).
2. **Google Sheets API**: Airflow uses the Google Sheets API to fetch real-time data.
3. **Airflow DAGs**: Automated workflows orchestrate the following steps:
    - Fetch new data.
    - Process the data (transformations, handling new entries).
    - Push the data to DuckDB (local processing) and MotherDuck (scalable cloud storage).
4. **Sentiment Analysis**: WhatsApp group chat data is analyzed for parental sentiment using NLP techniques.
5. **Machine Learning Models**: Predict student success based on available data and metadata.

---

## **How to Run the Project**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-repository-url.git
cd Prediction_Hackathon



Here’s the updated README with the additional information:

markdown
Copy code
# **Prediction Hackathon Project**

This project is developed for the Prediction Hackathon competition, where we are tasked with analyzing student performance data and related metadata to draw meaningful insights about their academic progress. The goal is to develop a solution that tracks and evaluates the academic performance of students, with integration for parental involvement and teacher feedback, using various tools and frameworks.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Data Collection](#data-collection)
3. [Tools and Libraries Used](#tools-and-libraries-used)
4. [Database Architecture](#database-architecture)
5. [Airflow DAGs](#airflow-dags)
6. [Data Flow](#data-flow)
7. [How to Run the Project](#how-to-run-the-project)

---

## **Project Overview**

This project focuses on analyzing student examination data and metadata like parental involvement and teacher feedback. The data is used to predict the potential success of students and how external factors such as parental sentiment (derived from WhatsApp group chats) and teacher assessments affect their academic performance.

We use Google Sheets to store data related to students, teachers, and exams. This data is then processed using Airflow, Google Sheets API, DuckDB, and MotherDuck for storage and analytics. Finally, we evaluate and predict insights from this data using various machine learning techniques, while also capturing how parental and teacher input correlates to student success.

### **Data Source**

The data used in this research was obtained from **Government Secondary School Manchok, Kaura LGA, Kaduna State, Nigeria**. The dataset contains academic records for students in **JSS3 (Junior Secondary School, Grade 9)**, covering one term of academic performance, specifically the third term. 

For privacy reasons, some of the students' names have been changed in this project. We adhered to strict confidentiality rules to protect the identities of the students involved in this study.

### **Methodology**

We employed several methodologies in this project:

1. **Research Method**: We conducted research to understand the educational system and parental involvement dynamics to guide our data collection and analysis.
2. **Data Mining**: Applied to derive insights from the available data and identify patterns in student performance.
3. **Data Engineering**: Focused on cleaning and transforming the data for further analysis.

---

## **Data Collection**

The main sources of data are:

- **Student Performance Data**: Contains the students' exam scores across different subjects, including Math, English, Science, etc. This data is fetched from a Google Sheet.
- **Parental Involvement Data**: Contains text from the school's WhatsApp group, where parents provide feedback, ask questions, or interact with teachers. Sentiment analysis is applied to this data to gauge parental involvement.
- **Teacher Feedback**: Data collected from teachers about student behavior and overall assessment throughout the term. This data is also stored in a Google Sheet.

We use **Google Sheets API** to pull this data into our system for further processing.

---

## **Tools and Libraries Used**

### **Data Collection**
- **Google Sheets API**: Used to fetch real-time data from the Google Sheets where the student, teacher, and parental involvement data is stored.
- **gspread**: A Python library that provides access to Google Sheets.
- **oauth2client**: A library used for OAuth 2.0 authentication.

### **Data Processing and Storage**
- **DuckDB**: Used for handling local queries and data storage.
- **MotherDuck**: Used for remote storage and querying large datasets, providing more scalability.
- **Pandas**: For efficient data manipulation and transformation.

### **Data Orchestration**
- **Apache Airflow**: For automating workflows, including fetching data from Google Sheets, transforming it, and pushing it to DuckDB and MotherDuck.

### **Deployment and Version Control**
- **Docker**: Used to containerize the application and ensure consistent runtime across different environments.
- **Git**: For version control of the project.

### **Libraries for Machine Learning and NLP**
- **NLTK (Natural Language Toolkit)**: Used for performing sentiment analysis on the parental chat data.
- **scikit-learn**: For training models to predict student success based on the data collected.

---

## **Database Architecture**

The data collected is stored in both **DuckDB** for local processing and **MotherDuck** for more scalable, cloud-based storage. The tables include:

- `Student_Exams_Record`: Contains student exam scores across multiple subjects.
- `Student_Profile`: Contains student demographic information.
- `Teacher_Data`: Includes data about teacher assessments of student behavior and performance.
- `Parent_Sentiment`: Contains analyzed data from WhatsApp group chats, including sentiment scores for each parent's involvement.

---

## **Airflow DAGs**

The following are the three main Airflow DAGs used in the project:

1. **Check MotherDuck Token**:
   - Ensures that the MotherDuck token is available in the environment.

2. **Update Student Exams Record**:
   - Fetches updated student exam data from Google Sheets.
   - Compares it with the existing records in DuckDB/MotherDuck.
   - Updates the data in the database if new data is found.

3. **Update Teacher Data & Student Profiles**:
   - Fetches new student and teacher data from Google Sheets.
   - Updates the `Student_Profile` and `Teacher_Data` tables if new data is found.

---

## **Data Flow**

The following steps describe the overall data flow of the project:

1. **Google Sheets**: The data is stored in multiple Google Sheets (one for exam scores, one for student profiles, one for teacher feedback).
2. **Google Sheets API**: Airflow uses the Google Sheets API to fetch real-time data.
3. **Airflow DAGs**: Automated workflows orchestrate the following steps:
    - Fetch new data.
    - Process the data (transformations, handling new entries).
    - Push the data to DuckDB (local processing) and MotherDuck (scalable cloud storage).
4. **Sentiment Analysis**: WhatsApp group chat data is analyzed for parental sentiment using NLP techniques.
5. **Machine Learning Models**: Predict student success based on available data and metadata.

---

## **How to Run the Project**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-repository-url.git
cd Prediction_Hackathon
2. Set Up Virtual Environment


python3 -m venv myenv
source myenv/bin/activate
3. Install Dependencies

pip install -r requirements.txt
4. Set Up Environment Variables
Make sure you set up the following in your .env file:

MOTHERDUCK_TOKEN=your_motherduck_token
GOOGLE_SHEETS_CREDENTIALS=path_to_your_secret_json_file

5. Run Airflow
Start the Airflow services:

astro dev start
Once Airflow is running, you can access the web interface at http://localhost:8081.

Monitor and run your DAGs from the web interface.

By following the above instructions, you should have the project up and running locally. The system will automatically update the student performance data, teacher data, and parental sentiment, which will provide insights into student success and help identify areas of improvement.

