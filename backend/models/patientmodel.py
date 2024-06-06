'''
Contains models that store data
'''
from pydantic import BaseModel
from ..Models import specialistmodel, notemodel, appointmentmodel, medicationmodel

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
    Gender: bool
    FirstNameContact: str
    LastNameContact: str
    EMailContact: str
    PhoneNumberContact: str
    Specialists: list[specialistmodel.Specialist]
    Notes: list[notemodel.Note]
    Medications: list[medicationmodel.Medication]
    Appointments: list[appointmentmodel.Appointment]
