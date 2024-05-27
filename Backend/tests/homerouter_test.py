'''
Tests for the home router
'''
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_homeurl():
    '''
    Tests if the api home url if available
    '''
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"true": "API is working!"}
