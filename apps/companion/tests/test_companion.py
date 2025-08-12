from fastapi.testclient import TestClient
from apps.companion.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_click_and_type():
    assert client.post("/click", json={"rect": [0,0,10,10]}).json()["status"] == "ok"
    assert client.post("/type", json={"text": "hello"}).json()["text"] == "hello"

def test_screenshot():
    data = client.post("/screenshot", json={}).json()
    assert "image" in data
