# tests/test_update.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.update
def test_update_todo_tags():
    response = client.put("/todos/2", json={
        "id": 2,
        "title": "Todo with updated tags",
        "description": "Updated tags",
        "done": True,
        "tags": ["important", "personal"]
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Todo with updated tags",
        "description": "Updated tags",
        "done": True,
        "tags": ["important", "personal"]
    }
