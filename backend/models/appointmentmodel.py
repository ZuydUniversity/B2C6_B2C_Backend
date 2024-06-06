'''
Contains models that store data
'''
import datetime
from pydantic import BaseModel
from ..Models import sessionmodel, patientmodel, specialistmodel

class Appointment(BaseModel):
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Session: sessionmodel.Session
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
