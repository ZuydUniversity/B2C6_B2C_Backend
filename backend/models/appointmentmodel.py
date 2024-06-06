'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel

class Appointment(BaseModel):
    ''' Class for the appointment.'''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    SessionId: int
    PatientId: int
    SpecialistId: int
