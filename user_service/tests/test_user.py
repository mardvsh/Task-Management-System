import pytest
from fastapi.testclient import TestClient
from user_service.main import app

client = TestClient(app)

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []
