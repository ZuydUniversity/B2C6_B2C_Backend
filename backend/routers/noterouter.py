'''
The router for the user which allows the user to register, 
login, logout and forgotpassword functionalities
'''
from requests import Request
from sqlalchemy.exc import IntegrityError, OperationalError, DataError, DatabaseError
from ..common import create_router
from ..models.notemodel import Note


router = create_router()

@router.post("/notes")
async def create_note(request: Request):
    '''
    Creates a note
    '''
    data = await request.json()
    name = data.get('name')
    session_id = data.get('sessionId')
    patient_id = data.get('patientId')
    specialist_id = data.get('specialistId')
    note = Note(Name=name, SessionId=session_id, PatientId=patient_id, SpecialistId=specialist_id)
    print(note) # This is temporary to satisfy PyLint
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die opslaan naar de database doet
        message = {"success": True, "result": "Note created successfully"}
    except IntegrityError as e:
        # Specifieke afhandeling voor IntegrityError
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        # Specifieke afhandeling voor OperationalError
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        # Specifieke afhandeling voor DataError
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        # Specifieke afhandeling voor andere database fouten
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return message

@router.patch("/notes/{note_id}")
async def patch_note(request: Request, note_id: int):
    '''
    Patches a note
    '''
    data = await request.json()
    ## Get right model from database with the note_id
    print(note_id) # This is temporary to satisfy PyLint
    note = Note()
    note.Name = data.get('name')
    note.SessionId = data.get('sessionId')
    note.PatientId = data.get('patientId')
    note.SpecialistId = data.get('specialistId')
    if data.get('debug') is None or data.get('debug') is False:
        debug = False
    else:
        debug = True
    if debug is not True:
        # Here the rest of the code is placed to save to the database.
        pass
    return note

@router.get('/notes')
async def get_notes():
    '''
    Gets all notes
    '''
    # Code here that gets all notes
    note = Note()
    note.Id = 1
    note.Name = "test"
    return note

@router.get('/notes/{note_id}')
async def get_note(note_id: int):
    '''
    Gets a note
    '''
    # Code here that gets a note
    print(note_id) # This is temporary to satisfy PyLint
    note = Note()
    note.Id = 1
    return note

@router.delete('/notes/{note_id}')
async def delete_note(note_id: int):
    '''
    Deletes a note
    '''
    # Code here that deletes a note
    print(note_id) # This is temporary to satisfy PyLint
    note = Note()
    return note
