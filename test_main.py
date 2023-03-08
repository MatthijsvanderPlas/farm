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
    assert b"<title>Home</title>" in response.data
    assert b"<h2>I am now a DevOps Engineer!</h2>" in response.data
