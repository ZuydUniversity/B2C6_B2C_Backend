'''
Contains models that store data
'''
from pydantic import BaseModel
from ..Models import sessionmodel, patientmodel, specialistmodel

class Note(BaseModel):
    '''Class for the notes.'''
    Id: int
    Name: str
    Session: sessionmodel.Session
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
