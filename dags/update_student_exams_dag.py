from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from sandbox import update_student_exams_record
from student_profile import update_student_profile_record
from teacher_data import update_teacher_data_record

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

# Task 1: Check if MotherDuck token exists
def check_motherduck_token():
    motherduck_token = os.getenv('MOTHERDUCK_TOKEN')
    if not motherduck_token:
        raise ValueError("MotherDuck token is missing")
    print("MotherDuck token is set!")

# Define the DAG
with DAG('update_student_exams_profile_teachers',
         default_args=default_args,
         schedule_interval='@daily',  # Adjust your schedule as needed
         catchup=False) as dag:

    # Task 1: Check if MotherDuck token is present in the environment
    check_motherduck_token_task = PythonOperator(
        task_id='check_motherduck_token',
        python_callable=check_motherduck_token
    )

    # Task 2: Update Student Exams Record (from sandbox.py)
    update_student_exams_task = PythonOperator(
        task_id='update_student_exams_task',
        python_callable=update_student_exams_record
    )

    update_student_profile_task = PythonOperator(
        task_id='update_student_profile_task',
        python_callable=update_student_profile_record
    )

    # Task 4: Update Teachers Data Record (from teacher_data.py)
    update_teacher_data_task = PythonOperator(
        task_id='update_teacher_data_task',
        python_callable=update_teacher_data_record
    )

    # Define task dependencies
    check_motherduck_token_task >> update_student_exams_task >> update_student_profile_task >> update_teacher_data_task
