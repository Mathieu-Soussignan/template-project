from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Projet 1 - API de gestion des patients"} # noqa


def test_get_utilisateurs():
    response = client.get("/utilisateurs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list) # noqa