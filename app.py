import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Streamlit page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load the diabetes model (Make sure "diabetes_model.sav" is in the same folder as this script)
try:
    with open("diabetes_model.sav", "rb") as file:
        diabetes_model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Model file 'diabetes_model.sav' not found! Place it in the same folder as 'app.py'.")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        " Disease Prediction System",
        ["Diabetes Prediction"],
        icons=["activity"]
    )

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")

    # User input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)

    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0)

    with col3:
        BloodPressure = st.number_input("Blood Pressure value", min_value=0)

    with col1:
        SkinThickness = st.number_input("Skin Thickness value", min_value=0)

    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0)

    with col3:
        BMI = st.number_input("BMI value", min_value=0.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value", min_value=0.0)

    with col2:
        Age = st.number_input("Age of the Person", min_value=1, step=1)

    # Prediction output
    diab_diagnosis = ""

    # Prediction button
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)
