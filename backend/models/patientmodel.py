'''
Contains models that store data
'''
from pydantic import BaseModel
from ..Models import specialistmodel, appointmentmodel, notemodel, medicationmodel

class Patient(BaseModel):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    Id: int
    FirstName: str
    LastName: str
    EMail: str
    Age: int
    PhoneNumber: str
    FirstNameContact: str
    LastNameContact: str
    EMailContact: str
    PhoneNumberContact: str
    Specialists: list[specialistmodel.Specialist]
    Notes: list[notemodel.Note]
    Medications: list[medicationmodel.Medication]
    Appointments: list[appointmentmodel.Appointment]
