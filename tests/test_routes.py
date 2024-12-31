import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_greet_with_name(client):
    response = client.get('/api/v1/greet?name=John')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello John!"}

def test_greet_without_name(client):
    response = client.get('/api/v1/greet')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello World!"}