'''
Contains models that store data
'''
from pydantic import BaseModel

class Note(BaseModel):
    '''Class for the notes.'''
    Id: int
    Name: str
    SessionId: int
    PatientId: int
    SpecialistId: int
