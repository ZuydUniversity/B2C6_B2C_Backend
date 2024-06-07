# pragma: no cover
'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel

class Appointment(BaseModel):
    '''
    Class for the appointment.
    
    Attributes:
        Id (Int): id of appointment
        Name (String): name of appointment
        StartDate (DateTime): starting date and time of appointment
        EndDate (DateTime): ending date and time of appointment
        SessionId (Int): id of the session part of this appointment
        PatientId (Int): The patient id who has this appointment
        SpecialistId (Int): The specialist id who has this appointment
    '''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    SessionId: int
    PatientId: int
    SpecialistId: int
