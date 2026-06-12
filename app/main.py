from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")

class Customer(BaseModel):
    city_tier: int
    age_group: int
    acquisition_channel: int
    loyalty_tier: int
    preferred_category: int
    marketing_consent: int

    recency_days: int
    frequency_180d: int
    monetary_180d: float

    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: float

    ticket_count_90d: int
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float

    days_since_signup: int
    sessions_30d: int
    product_views_30d: int
    cart_adds_30d: int
    wishlist_adds_30d: int
    abandoned_carts_30d: int
    email_opens_30d: int
    campaign_clicks_30d: int
    last_visit_days_ago: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):

    df = pd.DataFrame([customer.dict()])

    prob = float(model.predict_proba(df)[0][1])

    pred = int(prob >= 0.5)

    if prob >= 0.7:
        risk = "high"
    elif prob >= 0.4:
        risk = "medium"
    else:
        risk = "low"

    return {
        "churn_probability": round(prob, 3),
        "predicted_class": pred,
        "risk_level": risk,
        "risk_explanation":
        "Low recent activity and support interactions indicate elevated churn risk."
    }


@app.post("/batch_predict")
def batch_predict(customers: list[Customer]):

    df = pd.DataFrame([c.dict() for c in customers])

    probs = model.predict_proba(df)[:, 1]

    results = []

    for p in probs:
        results.append({
            "churn_probability": round(float(p), 3),
            "predicted_class": int(p >= 0.5)
        })

    return {"predictions": results}
