import pytest
from main import app


@pytest.fixture()
def client():
    client = app.test_client()
    return client


def test_homePage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello, world!</h1>" in response.data
