# pragma: no cover
'''
Contains models that store data
'''
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
