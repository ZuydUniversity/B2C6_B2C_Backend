'''
Contains models that store data
'''
from typing import List
from pydantic import BaseModel
from . import specialistmodel, notemodel, appointmentmodel, medicationmodel

class Patient(BaseModel):
    '''Class for the patients.'''
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
    Specialists: List[specialistmodel.Specialist]
    Notes: List[notemodel.Note]
    Medications: List[medicationmodel.Medication]
    Appointments: List[appointmentmodel.Appointment]
