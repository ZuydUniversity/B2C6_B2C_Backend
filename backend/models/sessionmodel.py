'''
Contains models that store data
'''
from pydantic import BaseModel
from ..Models import patientmodel, specialistmodel, appointmentmodel, notemodel
import datetime

class Session(BaseModel):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    Id: int
    Name: str
    StartDate: datetime.datetime
    EndDate: datetime.datetime
    Patient: patientmodel.Patient
    Specialist: specialistmodel.Specialist
    Appointments: appointmentmodel.Appointment
    Notes: notemodel.Note
