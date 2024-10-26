# tests/test_read.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.read
def test_get_todo_with_tags():
    response = client.get("/todos/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Todo with tags",
        "description": "This todo has tags",
        "done": False,
        "tags": ["urgent", "work"]
    }
