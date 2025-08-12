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
@app.get("/")
def root():
    return {"message": "Welcome to the Heart Disease Prediction API. Please visit /docs for API documentation."}
@app.get("/")
def root():
    return {
        "message": "Welcome to the Heart Disease Prediction API.",
        "documentation_url": "https://heart-disease-fastapi.onrender.com/docs",
        "note": "Please visit the documentation URL to explore and test the API endpoints."
    }
