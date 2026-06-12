from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict_invalid():
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_batch_predict_exists():
    response = client.post("/batch_predict", json=[])
    assert response.status_code == 200

def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
