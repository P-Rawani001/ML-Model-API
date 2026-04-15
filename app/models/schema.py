from pydantic import BaseModel, Field
from typing import Literal, Annotated

class UserInput(BaseModel):
    age: Annotated[int, Field(gt=0, lt=120)]
    annual_income: Annotated[float, Field(gt=0)]
    number_of_dependents: Annotated[int, Field(ge=0)]
    health_score: Annotated[float, Field(ge=0, le=100)]
    previous_claims: Annotated[int, Field(ge=0)]
    vehicle_age: Annotated[int, Field(ge=0)]
    credit_score: Annotated[int, Field(ge=300, le=850)]
    insurance_duration: Annotated[int, Field(ge=0)]

    gender: Literal["Male", "Female"]
    marital_status: Literal["Single", "Married", "Divorced"]
    education_level: Literal["High School", "Bachelor's", "Master's", "PhD"]
    occupation: Literal["Employed", "Self-Employed", "Unemployed"]
    location: Literal["Urban", "Rural", "Suburban"]
    policy_type: Literal["Basic", "Comprehensive", "Premium"]
    customer_feedback: Literal["Poor", "Average", "Good"]
    smoking_status: Literal["Yes", "No"]
    exercise_frequency: Literal["Daily", "Weekly", "Monthly", "Rarely"]
    property_type: Literal["House", "Apartment", "Condo"]