from fastapi import FastAPI
from pydantic import BaseModel
from prediction_helper import predict

app = FastAPI()

class CreditRequest(BaseModel):
    age: int
    income: float
    loan_amount: float
    loan_tenure_months: int
    avg_dpd_per_delinquency: float
    delinquency_ratio: float
    credit_utilization_ratio: float
    num_open_accounts: int
    residence_type: str
    loan_purpose: str
    loan_type: str

@app.get("/")
def home():
    return {"message": "Credit Risk Prediction API is running. Send a POST request to /predict"}

@app.post("/predict")
def predict_risk(data: CreditRequest):
    probability, credit_score, rating = predict(
        data.age, data.income, data.loan_amount, data.loan_tenure_months,
        data.avg_dpd_per_delinquency, data.delinquency_ratio,
        data.credit_utilization_ratio, data.num_open_accounts,
        data.residence_type, data.loan_purpose, data.loan_type
    )
    return {
        "default_probability": probability,
        "credit_score": credit_score,
        "rating": rating
    }
