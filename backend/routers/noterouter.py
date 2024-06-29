'''
The router for the notes wich allows the user to create, read, update and delete notes
'''
from fastapi import Depends, Request

from ..common import create_router
from ..models.note import Note
from ..models.specialist import Specialist
from sqlalchemy.orm import Session
from backend.database import create_database_session

router = create_router()

def get_db():
    db = create_database_session("")
    try:
        yield db
    finally:
        db.close()

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
        id=None,
        name=data.get('name'),
        description=data.get('description'),
        session = await getsessionfrom_database(data.get('sessionId')) or None,
        patient = await getpatientfrom_database(data.get('patientId')) or None,
        specialist = await getspecialistfrom_database(data.get('specialistId')) or None,
    )

    debug = data.get('debug') or False
    message = await save_notesdatabase(note, debug)
    
    return {"note": note, "message": message}

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
    response =  await get_specificnotedatabase(note_id)
    session = await getsessionfrom_database(data.get('sessionId'))
    patient = await getpatientfrom_database(data.get('patientId'))
    specialist = await getspecialistfrom_database(data.get('specialistId'))
    debug = data.get('debug') or False
    message = response["message"]
    note = response["note"]
    succes_message = {"success": True, "result": "Note retrieved successfully"}
    if message is not succes_message or note is not type(Note):
        if message is succes_message:
            return {"success": False, "result": "note is not type Note"}
        note.id = data.get('id')
        note.name = data.get('name')
        note.description = data.get('description')
        note.session = session
        note.patient = patient
        note.specialist = specialist

        save = await save_notesdatabase(note, debug)
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
    response = await get_notesdatabase()
    notes = response["notes"]
    message = response["message"]
    return {"notes": notes, "message": message}

@router.get('/notes/{note_id}')
async def get_note(note_id: int):
    '''
    Get router, call it with "api/notes/{note_id}".
    Make sure to specify the request type!
    Then it gets a note from the database
    It returns an message with success or failure.
    '''
    response = await get_specificnotedatabase(note_id)
    message = response["message"]
    note = response["note"]
    return {"note": note, "message": message}

@router.delete('/notes/{note_id}')
async def delete_note(requets: Request, note_id: int):
    '''
    Delete router, call it with "api/notes/{note_id}".
    Make sure to specify the request type!
    Then it deletes a note from the database
    It returns an message with success or failure.
    '''
    debug = await requets.json()
    debug = debug.get('debug') or False
    message = await deletefrom_notesdatabase(note_id, debug)
    return {"message": message}

async def save_notesdatabase(data, debug = False, db: Session = Depends(get_db)):
    '''
    Saves a note to the database
    '''
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        if bool(debug) is False:
            # Functie die notes opslaat naar de database
            print(data) # This is temporary to satisfy PyLint
            if data["id"] is not None or data["id"] != 0 or data["id"] != "0":
                db_note = db.query(Note).filter(Note.id == data["id"]).first()
                db_note.name = data["name"]
                db_note.description = data["description"]
                db_note.specialist = data["specialist"]
                db_note.specialist_id = data["specialist_"]["id"]
                db_note.session = data["session"]
                db_note.session_id = data["session"]["id"]
                db_note.patient = data["patient"]
                db_note.patient_id = data["patient"]["id"]
            else:
                db_note = Note(
                    id=0,
                    name=data["name"],
                    description=data["description"],
                    specialist=data["specialist"] if data["specialist"] is not None else None,
                    specialist_id=data["specialist"]["id"] if data["specialist"] is not None else None,
                    session=data["session"] if data["session"] is not None else None,
                    session_id=data["session"]["id"] if data["session"] is not None else None,
                    patient=data["patient"] if data["patient"] is not None else None,
                    patient_id=data["patient"]["id"] if data["patient"] is not None else None,
                )
                db.add(db_note)
            db.commit()
            db.refresh(db_note)
        message = {"success": True, "result": "Note saved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return message

async def get_notesdatabase(skip=0, limit=0, debug=False, db: Session = Depends(get_db)):
    '''
    Gets all notes
    Skip and Limit can be used to get a specific amount of notes instead of all for better performance
    '''
    # Code here that gets all notes from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        if debug is False:
            # Functie die alle notes ophaalt uit de database
            notes = []
            if limit == 0:
                notes = db.query(Note).all()
            else:
                notes = db.query(Note).limit(limit).offset(skip).all()
            message = {"success": True, "result": "Note retrieved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return {"notes": notes, "message": message}

async def get_specificnotedatabase(note_id, debug=False, db: Session = Depends(get_db)):
    '''
    Gets one specific note from the database
    '''
    # Code here that gets all notes from the database
    note = None
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die een specifieke note ophaalt uit de database
        if debug is False:
            note = db.query(Note).filter(Note.id == note_id).first()
        message = {"success": True, "result": "Note retrieved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return {"note": note, "message": message}

async def deletefrom_notesdatabase(note_id, debug = False, db: Session = Depends(get_db)):
    '''
    Deletes a note
    '''
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        if debug is False:
          # Functie die een specifieke note verwijderd uit de database
          print(note_id)
          db_user = db.query(Note).filter(Note.id == note_id).first()
          db.delete(db_user)
          db.commit()
        message = {"success": True, "result": "Note deleted successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return message

async def getsessionfrom_database(session_id, debug=False, db: Session = Depends(get_db)):
    '''
    Gets all sessions from the database
    '''
    # Code here that gets all sessions from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        print(session_id)
        # Code to get session from database by ID
        if debug is False:
            session = db.query(Session).filter(Session.id == session_id).first()
        message = {"success": True, "result": "Session retrieved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return {"session": session, "message": message}

async def getpatientfrom_database(patient_id, db: Session = Depends(get_db)):
    '''
    Geta patient from the database
    '''
    # Code here that gets all sessions from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        print(patient_id)
        # Code to get session from database by ID
        patient = 1
        message = {"success": True, "result": "Patient retrieved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return {"patient": patient, "message": message}

async def getspecialistfrom_database(specialist_id, db: Session = Depends(get_db)):
    '''
    Get a specialist from the database
    '''
    # Code here that gets all sessions from the database
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        print(specialist_id)
        # Code to get session from database by ID
        specialist = Specialist(
            1,
            "John",
            "doe",
            "eh",
            "EH",
            12,
            "BOE",
            None,
            None,
            None,
            None,
            )
        message = {"success": True, "result": "Specialist retrieved successfully"}
    except Exception as e:
        message = {"success": False, "error": f"Database Error: {e}"}
    return {"specialist": specialist, "message": message}