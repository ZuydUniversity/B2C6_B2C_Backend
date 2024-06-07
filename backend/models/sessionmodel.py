# pragma: no cover
'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel
from . import patientmodel, notemodel

class Session(BaseModel):
    '''
    Class for the sessions.
    
    Attributes:
        Id (Int): id of the session
        Name (String): name of the session
        StartDate (DateTime): starting date and time of the session
        EndDate (DateTime): ending date and time of the session
        Patient (Patient): the patient who partakes in the session
        SpecialistId (Int): the id of the specialist who partakes in the session
        AppointmentId (Int): the id of the appointment that this session belongs to
        Note (Note): a note that was made durring the session
    '''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Patient: patientmodel.Patient
    SpecialistId: int
    AppointmentId: int
    Note: notemodel.Note
