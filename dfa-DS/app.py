import streamlit as st
import os
import joblib

base = os.path.join(os.getcwd(), "objects")

# Load encoders
encoder = joblib.load(os.path.join(base, "OrdinalEncoder.pkl"))
label_encoder = joblib.load(os.path.join(base, "LabelEncoder.pkl"))
model = joblib.load(os.path.join(base, "LogisticRegression.pkl"))

st.set_page_config(page_title="student performace prediction")
st.title("Student performance prediction")

def use_model(data):
    categorical = data[1:]
    cat_encoded = encoder.transform([categorical])
    full_array = [data[0]] + cat_encoded[0].tolist()
    
    prediction = model.predict([full_array])

    pred_class = label_encoder.inverse_transform(prediction)[0]
    
    return pred_class
    
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Student personal details")
    age = st.number_input("Age", step=1, min_value=1, format="%i")
    gender = st.selectbox("Gender", options=["Female", "Male"])
    parent_edu = st.selectbox("Parental Education", options=["Higher Institution", "Primary", "Secondary"])
    house_inc = st.selectbox("Household income", options=["Low", "Medium", "High"])
    learn_dis = st.selectbox("Learning Disability", options=["Yes", "No"])
    
with col2:
    st.subheader("Academic activity details")
    extra_curr = st.selectbox("Participation in Extracurricular Activities", options=["Yes", "No"])
    study_habit = st.selectbox("Study Habits", options=["Good", "Moderate", "Poor"])
    learn_access = st.selectbox("Has Access to Learning Materials", options=["Yes", "No"])
    internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
    class_engage = st.selectbox("Engagement in Class", options=["High", "moderate", "low"])
  
with col3:
    st.subheader("Psychological details")  
    emotion = st.selectbox("Emotional Well-Being", options=["Good", "Moderate", "Poor"])
    peer_inf = st.selectbox("Peer Influence", options=["Positive", "Neutral", "Negative"])
    teach_stud = st.selectbox("Teacher-Student Interaction", options=["Frequent", "Rare"])
    parent_support = st.selectbox("Support from Parents", options=["Good", "Moderate", "Poor"])
    submit = st.button("Predict performance")
    
data = [age, gender, parent_edu, house_inc, learn_dis, extra_curr, study_habit, learn_access, internet_access, class_engage, emotion, peer_inf, teach_stud, parent_support]

if submit:
    performance = use_model(data=data)
    st.success(f"Predicted student's performance: {performance}")