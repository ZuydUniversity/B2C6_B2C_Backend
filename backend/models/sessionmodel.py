'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel
from ..Models import patientmodel, specialistmodel, appointmentmodel, notemodel

class Session(BaseModel):
    '''Class for the sessions.'''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
    Appointments: appointmentmodel.Appointment
    Notes: notemodel.Note
