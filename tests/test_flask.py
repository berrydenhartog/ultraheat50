import pytest
from uh50 import create_app

@pytest.fixture()
def app():
    app = create_app({
        "TESTING": True,
        "CACHE_TYPE": "SimpleCache",
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_home(client):
    response = client.get("/")
    assert response.status_code == 200