# Monitoring Plan

## Data Drift Monitoring

The distributions of important features such as recency_days, frequency_180d, monetary_180d, and ticket_count_90d should be monitored regularly. Significant changes may indicate data drift.

## Prediction Distribution Monitoring

Track the percentage of customers predicted as high-risk, medium-risk, and low-risk. Sudden shifts may indicate model degradation.

## Business Outcome Monitoring

Compare predicted churn risk with actual customer retention outcomes. Track retention campaign effectiveness and churn reduction metrics.

## API Error Monitoring

Monitor API response times, failed requests, validation errors, and server exceptions.

## Retraining Triggers

The model should be retrained if:

* Data drift exceeds acceptable thresholds.
* Prediction distributions change significantly.
* Model performance declines on recent customer data.
* Business KPIs show reduced prediction usefulness.

## Responsible Use Note

The API output should support retention decisions but should not be used as the sole basis for customer treatment. Predictions represent probabilities, not certainty. Customers should not be unfairly targeted, excluded, or penalized solely because they are predicted to churn. Human review and business judgment should always accompany model outputs.
