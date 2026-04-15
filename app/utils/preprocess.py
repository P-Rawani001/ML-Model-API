import pandas as pd
from app.models.schema import UserInput

def preprocess(data: UserInput) -> pd.DataFrame:
    return pd.DataFrame([{
        "Age": data.age,
        "Annual Income": data.annual_income,
        "Number of Dependents": data.number_of_dependents,
        "Health Score": data.health_score,
        "Previous Claims": data.previous_claims,
        "Vehicle Age": data.vehicle_age,
        "Credit Score": data.credit_score,
        "Insurance Duration": data.insurance_duration,
        "Gender": data.gender,
        "Marital Status": data.marital_status,
        "Education Level": data.education_level,
        "Occupation": data.occupation,
        "Location": data.location,
        "Policy Type": data.policy_type,
        "Customer Feedback": data.customer_feedback,
        "Smoking Status": data.smoking_status,
        "Exercise Frequency": data.exercise_frequency,
        "Property Type": data.property_type,
    }])