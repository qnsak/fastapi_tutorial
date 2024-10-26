# tests/test_delete.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.delete
def test_delete_todo_with_tags():
    response = client.delete("/todos/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Todo with updated tags",
        "description": "Updated tags",
        "done": True,
        "tags": ["important", "personal"]
    }

    response = client.get("/todos/2")
    assert response.status_code == 404
