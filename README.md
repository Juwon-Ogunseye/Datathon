# **Prediction Hackathon Project**

[System Architecture](https://github.com/user-attachments/assets/bc93575d-ad16-4277-baee-2cae220881f3)

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

# Data Science, Machine Learning and Artificial Intelligence
The data prepared were faetched directly into a Jupyter notebook, for model training.

### Data explanation
There are three datasets, each from a different table extracted from the DB.<br>
The datasets are:
* Student performance data
* Student profile data
* Teachers' data

Each will be explained with the data overview seem so far, more insights will be obtained later on in the notebook
#### Student performance data
This dataset includes names of 40 students from a school in Nigeria, their test scores in certain subjects looked into, it also informed us of the gender of the students

***Descision:*** The scores can be merged together to get the overall average score of each student, names data removed, as they are neither relevant to the analysis, nor to the model to be built. The gender column should remain, unless otherwise necessary.

#### Student profile data
This dataset includes student names, average scores, and gender (all can be found in the first data) with more columns that are beneficial to model building and EDA in general.

***Decision:*** Once it is ascertained that the average score here matches with the average score that is intended to be calculated from the first data, then, all the information in the first data can be ignored as they have been repeated in the second data with more relevant columns, even. Otherwise, it (the intended average) will still be calculated and added to the second dataset. This data will be used for model training, to predict students' performance based on their data.

#### Teachers' data
This dataset contains information about 20 teachers in the same school as the sample students, it has information regarding their names, years of experience, and many more relevant columns, good for insights to help the school improve students performance, but model training is not necessary.

***Decision:*** This data is good to find some valuable insights on what to improve on, but no model training is required.

### ML
A machine learning classification model is then devoloped based on the student profile data and exam data.
The details can be found in the used [Jupyter Notebook](./dfa-DS/DFA24%20model%20notebook.ipynb)<br>

Also, the model is deployed using [streamlit](https://streamlit.io), the deployed app can be accessed [here](https://dfa24-students-performance-lambda.streamlit.app).

#### Libraries for machine learning and deployment
* Pandas - For data cleaning, and preparation
* DuckDB - For loading the data directly from the database
* Scikit-Learn - For building the machine learning model
* Streamlit - For creating the web interface

### AI solution
Link to app: https://teacher-question-guide-dfa24.streamlit.app/ <br>
It is part of the requirement to help the school help their students improve their overall performance, to that end, an AI application has also been deployed to help teachers easily set up practice sessions for students, simply by uploading relevant class document(s).

###### About
This tool allows teachers set up practice question and answer session for their students in real-time, simply by uploading the class document(.pdf or .docx). They get to present the questions to the students for their opinion, and once an answer is agreed upon, it is enteredd into the AI, the AI evaluates the response and gives its response on whether the answer is correct or fully suffices as an answer. Teachers can also use the "reveal answer" panel to see the correct from the notebook.<br>
Teachers can also use them to streamline the setting of the usual exam/test/quiz questions. Once the questions are generated, they can download the question and answer pairs as a csv file, that can be referenced later.
The teachers were made a focus for the usage of this tool due to the fact that only 22.5% of the students (according to the data) has access to the internet at home, just so no one is left out from the benefit.<br>

###### Use case
Good way to engage students after lessons to test for their understanding of the subject. Also good for time-to-time revision.

###### Future additions
* Support longer documents
* Support more document formats

###### Demo video
https://github.com/user-attachments/assets/c613e5e5-a689-48e7-899c-8d359cdc37e9

#### Technologies used for the AI app
* Python - The programming language used
* python-docx - To load docx file when uploaded
* PyPDF2 - To load PDFs when uploaded
* Pandas - To convert the data into csv format
* Langchain - As an interface to access the AI (LLM) and other several AI development tools
* Pydantic - for structured AI output
* Google Gemini LLMs (Gemini Pro and Gemini 1.5 Flash)
* Streamlit - To create the web interface