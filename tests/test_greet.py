# tests/test_greet.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_greet_name():
    # 測試 API 當輸入名字 "Alice" 時的回應
    response = client.get("/greet?name=Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Alice, hello"}

    # 測試 API 當輸入名字 "Bob" 時的回應
    response = client.get("/greet?name=Bob")
    assert response.status_code == 200
    assert response.json() == {"message": "Bob, hello"}
