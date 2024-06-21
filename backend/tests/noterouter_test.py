'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# Test data
test_note = {
    "id": 1,
    "name": "Test",
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
    note, response = client.post("/api/notes", json=test_note)
    assert response.status_code == 200
    assert response.json() == {"success": True, "result": "Note created successfully"}
    assert note.json() == test_note

async def patch_note_test():
    '''
    Test if the patching of the notes works.
    '''
    note, response = client.patch("/api/notes/2", json=test_note)
    assert response.status_code == 200
    assert response.json() == {"success": True, "result": "Note created successfully"}
    assert note.json() == test_note

async def get_notes_test():
    '''
    Test if the getting of the notes works.
    '''
    notes, response = client.get("/api/notes")
    assert response.status_code == 200
    assert response.json() == {"success": True, "result": "Note created successfully"}
    assert notes.json() is not None

async def get_note_test():
    '''
    Test if the getting of the note works.
    '''
    note, response = client.get("/api/notes/1")
    assert response.status_code == 200
    assert response.json() == {"success": True, "result": "Note created successfully"}
    assert note.json() is not None

async def delete_note_test():
    '''
    Test if the deleting of the notes works.
    '''
    response = client.delete("/api/notes/1")
    assert response.status_code == 200
    assert response.json() == {"success": True, "result": "Note created successfully"}

