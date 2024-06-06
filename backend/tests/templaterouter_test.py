'''
Tests for the home router
'''
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_template():
    '''
    Tests if the api get template if available
    '''
    response = client.get("/api/template/")
    assert response.status_code == 200
    assert response.json() == {"id":1,"name":"Homoerectus","address":"USA"}
