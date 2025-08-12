from fastapi import FastAPI
from joblib import load
from app.schemas import HeartDiseaseInput

app = FastAPI()

model = load("model/heart_model.joblib")

features = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak", "slope",
    "ca", "thal"
]

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/info")
def info():
    return {
        "model": "RandomForestClassifier",
        "features": features
    }

@app.post("/predict")
def predict(data: HeartDiseaseInput):
    input_data = [[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]]
    prediction = model.predict(input_data)[0]
    return {"heart_disease": bool(prediction)}
