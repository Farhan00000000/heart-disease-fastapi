# Heart Disease Prediction API

## Project Structure

- app/ - FastAPI code
- model/ - saved model file
- Dockerfile - Docker instructions
- docker-compose.yml - Docker compose config
- requirements.txt - Python dependencies

## Run Locally

Build and run the app:

docker-compose build
docker-compose up

Access Swagger UI: http://localhost:8000/docs

## Endpoints

- GET /health - Health check
- GET /info - Model info and features
- POST /predict - Predict heart disease presence (send JSON with features)

## Deployment

Deployed on Render: [Your Live URL Here]
