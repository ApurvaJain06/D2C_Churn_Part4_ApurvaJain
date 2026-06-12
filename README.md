# D2C_Churn_Part4_ApurvaJain
# D2C Churn Prediction API

## Project Overview

This project provides a FastAPI-based churn prediction service for a D2C business. The API loads a trained Random Forest churn prediction model and returns churn probabilities and risk levels for customers.

The service supports:

* Health check endpoint
* Single customer prediction
* Batch customer prediction
* Input validation using Pydantic

---

## Project Structure

D2C_Churn_Part4_ApurvaJain/

app/
main.py# D2C_Churn_Part4_ApurvaJain


## Project Overview
Predict customer churn using a Random Forest model.

## Repository Structure

app/main.py
model.pkl
requirements.txt
test_api.py
monitoring_plan.md

## Setup

pip install -r requirements.txt

## Run API

uvicorn app.main:app --reload

## Endpoints

GET /health

POST /predict

POST /batch_predict


model.pkl

requirements.txt

test_api.py

monitoring_plan.md

README.md

---

## Setup Instructions

Clone the repository:

git clone <repository-link>

cd D2C_Churn_Part4_ApurvaJain

Install dependencies:

pip install -r requirements.txt

---

## Run the API

uvicorn app.main:app --reload

API documentation:

http://127.0.0.1:8000/docs

---

## Endpoints

GET /health

Returns API health status.

POST /predict

Returns churn prediction for a single customer.

POST /batch_predict

Returns churn predictions for multiple customers.

---

## Sample Request

POST /predict

{
"recency_days": 90,
"frequency_180d": 1,
"monetary_180d": 500
}

---

## Sample Response

{
"churn_probability": 0.82,
"predicted_class": 1,
"risk_level": "high",
"risk_explanation": "Customer shows low activity and low purchase frequency."
}

---

## Running Tests

pytest test_api.py

---

## Model Notes

Model used: RandomForestClassifier

Training data source: rfm_modeling_snapshot.csv

Target variable: churn_next_60d

The model uses only snapshot-time features to avoid data leakage.
