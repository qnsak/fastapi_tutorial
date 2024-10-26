# tests/test_create.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.create
def test_create_todo_with_tags():
    response = client.post("/todos", json={
        "id": 2,
        "title": "Todo with tags",
        "description": "This todo has tags",
        "done": False,
        "tags": ["urgent", "work"]
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Todo with tags",
        "description": "This todo has tags",
        "done": False,
        "tags": ["urgent", "work"]
    }

@pytest.mark.create
def test_create_todo_without_tags():
    response = client.post("/todos", json={
        "id": 3,
        "title": "Todo without tags",
        "description": "This todo has no tags",
        "done": False
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "title": "Todo without tags",
        "description": "This todo has no tags",
        "done": False,
        "tags": []
    }
