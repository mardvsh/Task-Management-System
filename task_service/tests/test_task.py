import pytest
from fastapi.testclient import TestClient
from task_service.main import app

client = TestClient(app)

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.json() == []
