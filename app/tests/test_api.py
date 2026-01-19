from fastapi import testclient
from main import app

client = testclient.TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_create_item():
    response = client.post("/items?name=Test&description=Mon test")
    assert response.status_code == 200
    assert response.json()["name"] == "Test"

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

