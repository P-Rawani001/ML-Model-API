import joblib
import os
from fastapi.responses import JSONResponse
from app.utils.preprocess import preprocess

MODEL_PATH = os.path.join("app", "ml", "model.pkl")
model = joblib.load(MODEL_PATH)

def predict_premium(data):
    try:
        processed = preprocess(data)
        pred = model.predict(processed)[0]
        return {"prediction": round(float(pred), 2)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})