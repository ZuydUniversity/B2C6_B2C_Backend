from fastapi.testclient import TestClient
from Backend.main import app

client = TestClient(app)

def test_homeurl():
    response = client.get("/api/")  # Makes the request to the API url.
    assert response.status_code == 200  # Checks if the status code is 200.
    assert response.json() == {"true": "API is working!"}  # Checks if the response from the url is correct.