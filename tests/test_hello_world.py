from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_login():
    resp = client.get(
        "/",
    )
    print(f"\n\t response: {resp.text}")
    assert resp.status_code == 200
