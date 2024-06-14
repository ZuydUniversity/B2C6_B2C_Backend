'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# Test data
test_note = {
    "id": 2,
    "name": "This is the content off an note",
    "sessionId": 1,
    "patientId": 1,
    "specialistId": 1,
    "debug": True
}
async def create_note():
    '''
    Test if logging in works 
    '''
    response = client.post("/api/notes", json=test_note)
    assert response.status_code == 200
    assert response.json()["id"] == test_note["id"]
    assert response.json()["name"] == test_note["name"]
    assert response.json()["patientId"] == test_note["patientId"]
    assert response.json()["sessionId"] == test_note["sessionId"]
    assert response.json()["specialistId"] == test_note["specialistId"]
