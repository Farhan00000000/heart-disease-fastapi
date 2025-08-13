# Heart Disease Prediction API

This project features a FastAPI application that predicts the presence of heart disease based on patient clinical data. The backend uses a RandomForestClassifier model trained on the Heart Disease Dataset. The application is fully containerized with Docker for easy deployment and scalability. It is currently deployed and live on Render.

---

## Project Structure

- `app/` — FastAPI application source code  
- `model/` — Serialized machine learning model file (`heart_model.joblib`)  
- `Dockerfile` — Instructions to build the Docker image  
- `docker-compose.yml` — Docker Compose configuration for easy local development  
- `requirements.txt` — Python dependencies  
- `README.md` — Project documentation  

---

## Running the Application Locally

To run the application on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/Farhan00000000/heart-disease-fastapi.git
    cd heart-disease-fastapi
    ```

2. Build and start the Docker containers:

    ```bash
    docker-compose build
    docker-compose up
    ```

3. Open your web browser and navigate to:

    ```
    http://localhost:8000/docs
    ```

    This opens the Swagger UI, an interactive API documentation where you can test all the endpoints.

---

## API Endpoints

- **GET `/health`**  
  Returns a simple health check to confirm the server is running.

- **GET `/info`**  
  Returns metadata about the model, including the algorithm type and the list of features it expects.

- **POST `/predict`**  
  Accepts patient data as JSON input and returns whether heart disease is predicted (`true` or `false`).

### Example JSON Payload for `/predict`
***
```
{
  "age": 60,
  "sex": 1,
  "cp": 2,
  "trestbps": 130,
  "chol": 240,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
```
***

---

## Deployment

The application is deployed live on Render and accessible at:  
[https://heart-disease-fastapi.onrender.com](https://heart-disease-fastapi.onrender.com)

You can explore and interact with the API using the Swagger UI available at:  
[https://heart-disease-fastapi.onrender.com/docs](https://heart-disease-fastapi.onrender.com/docs)

Make sure that Docker Desktop is on in your machine.

---

## Author

[Farhan00000000](https://github.com/Farhan00000000)

---

## Project

FastAPI + Docker + Deployment (Heart Disease Prediction)

---

## License

This project is open-source and available under the MIT License.
