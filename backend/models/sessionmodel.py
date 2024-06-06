'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel
from . import patientmodel, notemodel

class Session(BaseModel):
    '''Class for the sessions.'''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Patient: patientmodel.Patient
    SpecialistId: int
    AppointmentsId: int
    Notes: notemodel.Note
