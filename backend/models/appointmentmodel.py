'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel
from Backend.Models import sessionmodel, patientmodel, specialistmodel

class Appointment(BaseModel):
    ''' Class for the appointment.'''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Session: sessionmodel.Session
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
