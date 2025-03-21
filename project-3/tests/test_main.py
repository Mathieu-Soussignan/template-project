# import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Projet 3 - API d'orchestration"}


def test_get_utilisateurs():
    response = client.get("/get-patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_predict_charges():
    payload = {
        "age": 40,
        "bmi": 22.0,
        "children": 1,
        "sex": "female",
        "smoker": "no",
        "region": "northwest"
    }
    response = client.post("/predict-charge", json=payload)
    assert response.status_code == 200
    assert "predicted_charges" in response.json()