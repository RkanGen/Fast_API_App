from fastapi.testclient import TestClient
from main1 import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert "id" in response.json()

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
