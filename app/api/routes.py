from fastapi import APIRouter
from app.models.schema import UserInput
from app.services.prediction import predict_premium

router = APIRouter()

@router.post("/predict")
def predict(data: UserInput):
    return predict_premium(data)

@router.get("/health")
def health():
    return {"status": "ok"}