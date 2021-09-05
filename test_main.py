from fastapi.testclient import TestClient
from main import app


client = TestClient(app)
version = "1.0.1"


def test_app_default():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Test-app": version}


def test_app_id_int():
    response = client.get("/12")
    assert response.status_code == 200
    assert response.json() == {"accountID": 12, "version": version}


def test_app_id_str():
    response = client.get("/test")
    assert response.status_code == 422


def test_app_data():
    response = client.get("/12/data")
    assert response.status_code == 200
    assert response.json() != {"accountID": 12}
