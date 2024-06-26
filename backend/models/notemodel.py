'''
Contains models that store data
'''
from sqlalchemy.exc import IntegrityError, OperationalError, DataError, DatabaseError
from pydantic import BaseModel

class Note(BaseModel):
    '''
    Class for the notes.
    
    Attributes:
        Id (Int): id of the note
        Name (String): name of the note
        SessionId (Int): id of the session the note is from
        PatientId (Int): id of patient of which the note was made
        SpecialistId (Int): id of specialist who made the node
    '''
    Id: int
    Name: str
    SessionId: int
    PatientId: int
    SpecialistId: int

async def save_notesdatabase(data):
    '''
    Saves a note to the database
    '''
    message =  {"success": False, "error": "An unexpected error occurred"}
    try:
        # Functie die notes opslaat naar de database
        print(data) # This is temporary to satisfy PyLint
        message = {"success": True, "result": "Note saved successfully"}
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
        notes = []
        notes.append(temp_note)
        message = {"success": True, "result": "Note retrieved successfully"}
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
        message = {"success": True, "result": "Note retrieved successfully"}
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
        message = {"success": True, "result": "Note deleted successfully"}
    except IntegrityError as e:
        message = {"success": False, "error": "IntegrityError: " + str(e)}
    except OperationalError as e:
        message = {"success": False, "error": "OperationalError: " + str(e)}
    except DataError as e:
        message = {"success": False, "error": "DataError: " + str(e)}
    except DatabaseError as e:
        message = {"success": False, "error": "DatabaseError: " + str(e)}
    return message
