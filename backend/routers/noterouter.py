'''
The router for the notes wich allows the user to create, read, update and delete notes
'''
from fastapi import Request
from sqlalchemy.exc import IntegrityError, OperationalError, DataError, DatabaseError
from ..common import create_router
from ..models.notemodel import Note
from typing import Dict


router = create_router()

@router.post("/notes")
async def create_note(request: Request):
    '''
    Create router, call it with "api/notes" and with an JSON file with all the data.
    Make sure to specify the request type!
    This then creates a note and saves it to the database.
    It returns an message with success or failure.
    '''
    data = await request.json()
    note = Note(
        Id=data.get('id'),
        Name=data.get('name'),
        SessionId=data.get('sessionId'),
        PatientId=data.get('patientId'),
        SpecialistId=data.get('specialistId')
    )
    if bool(data.get('debug')) is False or bool(data.get('debug')) is None:
        save = save_notesdatabase(note)
    else:
        save = {"message": {"success": "True", "result": "Note created successfully"}, "note": note}
    return save

@router.patch("/notes/{note_id}")
async def patch_note(request: Request, note_id: int):
    '''
    Patch router, call it with "api/notes/{note_id}" and with an JSON file with all the data.
    Make sure to specify the request type!
    Then it updates the data and saves it to the database.
    It returns an message with success or failure.
    '''
    # This is temporary to satisfy PyLint
    data = await request.json()
    response =  get_specificnotedatabase(note_id)
    message = response['message']
    note = response['note']	
    succes_message = {"success": True, "result": "Note created successfully"}
    if message is not succes_message or note is not type(Note):
        if message is succes_message:
            return {"success": False, "result": "note is not type Note"}
        else:
            return message
    note.Name = data.get('name')
    note.SessionId = data.get('sessionId')
    note.PatientId = data.get('patientId')
    note.SpecialistId = data.get('specialistId')
    if data.get('debug') is False or data.get('debug') is None:
        save = save_notesdatabase(note)
    else:
        save = {"success": True, "result": "Note created successfully"}
    return {"note": note, "message": save}

@router.get('/notes')
async def get_notes():
    '''
    Get router, call it with "api/notes".
    Make sure to specify the request type!
    Then it gets all the notes from the database
    It returns an message with success or failure.
    '''
    # Code here that gets all notes
    response = get_notesdatabase()
    return {"notes": response['notes'], "message": response['message']}

@router.get('/notes/{note_id}')
async def get_note(note_id: int):
    '''
    Get router, call it with "api/notes/{note_id}".
    Make sure to specify the request type!
    Then it gets a note from the database
    It returns an message with success or failure.
    '''
    response =  get_specificnotedatabase(note_id)
    message = response['message']
    note = response['note']
    succes_message = {"success": True, "result": "Note created successfully"}
    if message is not succes_message or note is not type(Note):
        if message is succes_message:
            return {"success": False, "result": "note is not type Note"}
        else:
            return message
    save = save_notesdatabase(note)
    return {"note": note, "message": save}

@router.delete('/notes/{note_id}')
async def delete_note(note_id: int):
    '''
    Delete router, call it with "api/notes/{note_id}".
    Make sure to specify the request type!
    Then it deletes a note from the database
    It returns an message with success or failure.
    '''
    save = deletefrom_notesdatabase(note_id)
    return save

async def save_notesdatabase(data):
    '''
    Saves a note to the database
    '''
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die notes opslaat naar de database
        print(data) # This is temporary to satisfy PyLint
        message = {"success": True, "result": "Note created successfully"}
    except IntegrityError as e:
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return message

async def get_notesdatabase():
    '''
    Gets all notes
    '''
    # Code here that gets all notes from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die alle notes ophaalt uit de database
        temp_note = Note(Id=1, Name="test", SessionId=1, PatientId=1, SpecialistId=1)
        notes = [temp_note]
        message = {"success": True, "result": "Note created successfully"}
    except IntegrityError as e:
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return {"notes": notes, "message": message}

async def get_specificnotedatabase(note_id):
    '''
    Gets one specific note from the database
    '''
    # Code here that gets all notes from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die een specifieke note ophaalt uit de database
        print(note_id)
        note= Note(Id=1, Name="test", SessionId=1, PatientId=1, SpecialistId=1)
        message = {"success": True, "result": "Note recieved successfully"}
    except IntegrityError as e:
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return {"note": note, "message": message}

async def deletefrom_notesdatabase(note_id):
    '''
    Deletes a note
    '''
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die een specifieke note verwijderd uit de database
        print(note_id)
        message = {"success": True, "result": "Note recieved successfully"}
    except IntegrityError as e:
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return message
