'''
The router for the user which allows the user to register, 
login, logout and forgotpassword functionalities
'''
from requests import Request
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

    Note(Name=name, SessionId=session_id, PatientId=patient_id, SpecialistId=specialist_id)
    # Here the rest of the code is placed to save to the database.

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
    # Here the rest of the code is placed to save to the database.