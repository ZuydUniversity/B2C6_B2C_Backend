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
async def create_note_test():
    '''
    Test if the creating of the notes works.
    It doesn't write to the database however, 
    It takes the variables out of the JSON then creates an class for it. 
    Then it returns that class as an JSON.
    '''
    response = client.post("/api/notes", json=test_note)
    assert response.status_code == 200
    assert response.json()["id"] == test_note["id"]
    assert response.json()["name"] == test_note["name"]
    assert response.json()["patientId"] == test_note["patientId"]
    assert response.json()["sessionId"] == test_note["sessionId"]
    assert response.json()["specialistId"] == test_note["specialistId"]

async def patch_note_test():
    '''
    Test if the patching of the notes works.
    '''
    response = client.patch("/api/notes/2", json=test_note)
    assert response.status_code == 200
    assert response.json()["name"] == test_note["id"]

async def get_notes_test():
    '''
    Test if the getting of the notes works.
    '''
    response = client.get("/api/notes")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    assert response.json()[1]["name"] == "test"

async def get_note_test():
    '''
    Test if the getting of the note works.
    '''
    response = client.get("/api/notes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

async def delete_note_test():
    '''
    Test if the deleting of the notes works.
    '''
    response = client.delete("/api/notes/1")
    assert response.status_code == 200
