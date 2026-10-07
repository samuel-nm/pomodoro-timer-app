from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Pomodoro Timer API is running"}


def test_get_stages():
    response = client.get("/stages")
    assert response.status_code == 200
    assert "work" in response.json()["stages"]


def test_get_stage_not_found():
    response = client.get("/stages/invalid_stage")
    assert response.status_code == 404
