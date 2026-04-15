import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Insurance Premium Predictor", page_icon="🛡️", layout="centered")
st.title("🛡️ Insurance Premium Amount Predictor")
st.markdown("Fill in your details to get your estimated annual insurance premium.")

# Personal Info
st.subheader("👤 Personal Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=119, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])

with col2:
    occupation = st.selectbox("Occupation", ["Employed", "Self-Employed", "Unemployed"])
    location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
    number_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=20, value=0)
    annual_income = st.number_input("Annual Income ($)", min_value=1.0, value=50000.0, step=1000.0)

# Health
st.subheader("🏥 Health & Lifestyle")
col3, col4 = st.columns(2)

with col3:
    health_score = st.slider("Health Score", 0.0, 100.0, 70.0)
    smoking_status = st.selectbox("Smoking Status", ["No", "Yes"])

with col4:
    exercise_frequency = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly", "Rarely"])
    customer_feedback = st.selectbox("Customer Feedback", ["Good", "Average", "Poor"])

# Insurance
st.subheader("📋 Insurance & Assets")
col5, col6 = st.columns(2)

with col5:
    policy_type = st.selectbox("Policy Type", ["Basic", "Comprehensive", "Premium"])
    insurance_duration = st.number_input("Insurance Duration", 0, 50, 5)
    previous_claims = st.number_input("Previous Claims", 0, 50, 0)

with col6:
    credit_score = st.number_input("Credit Score", 300, 850, 650)
    vehicle_age = st.number_input("Vehicle Age", 0, 50, 3)
    property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])

if st.button("Predict"):
    data = {
        "age": int(age),
        "annual_income": float(annual_income),
        "number_of_dependents": int(number_of_dependents),
        "health_score": float(health_score),
        "previous_claims": int(previous_claims),
        "vehicle_age": int(vehicle_age),
        "credit_score": int(credit_score),
        "insurance_duration": int(insurance_duration),
        "gender": gender,
        "marital_status": marital_status,
        "education_level": education_level,
        "occupation": occupation,
        "location": location,
        "policy_type": policy_type,
        "customer_feedback": customer_feedback,
        "smoking_status": smoking_status,
        "exercise_frequency": exercise_frequency,
        "property_type": property_type,
    }

    res = requests.post(API_URL, json=data)

    if res.status_code == 200:
        st.success(f"💰 Premium: ${res.json()['prediction']}")
    else:
        st.error("Error from backend")