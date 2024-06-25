'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_note():
    '''
    Test if the creating of the notes works.
    It doesn't write to the database however, 
    It takes the variables out of the JSON then creates an class for it. 
    Then it returns that class as an JSON.
    '''
    test_note = {
        "id": 1,
        "name": "Test Note",
        "sessionId": 1,
        "patientId": 1,
        "specialistId": 1,
        "debug": True
    }

    response = client.post("/api/notes", json=test_note)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["message"] == {"success": True, "result": "Note created successfully"}
    assert response_json["note"]["Name"] == "Test Note"

def test_patch_note():
    '''
    Test if the patching of the notes works.
    '''
    test_note = {
        "name": "Test Note",
        "sessionId": "session123",
        "patientId": "patient456",
        "specialistId": "specialist789",
        "debug": True
    }
    response = client.patch("/api/notes/2", json=test_note)
    assert response.status_code == 200
    assert response.json()['message'] == {"success": True, "result": "Note patched successfully"}
    assert response.json()['note'] == test_note

def test_get_notes():
    '''
    Test if the getting of the notes works.
    '''
    response = client.get("/api/notes")
    assert response.status_code == 200
    assert response.json()["message"] == {"success": True, "result": "Note retrieved successfully"}

def test_get_note():
    '''
    Test if the getting of the note works.
    '''
    response = client.get("/api/notes/1")
    assert response.status_code == 200
    assert response.json()["message"] == {"success": True, "result": "Note retrieved successfully"}

def test_delete_note():
    '''
    Test if the deleting of the notes works.
    '''
    response = client.delete("/api/notes/1")
    assert response.status_code == 200
    assert response.json()["message"] == {"success": True, "result": "Note deleted successfully"}
