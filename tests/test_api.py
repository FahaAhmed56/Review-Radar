from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_predict():
    response = client.post("/analyze", json={"review": "Amazing product works perfectly"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"

def test_reject_empty():
    assert client.post("/analyze", json={"review": ""}).status_code == 422
