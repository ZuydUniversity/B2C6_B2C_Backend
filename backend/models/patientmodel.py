# pragma: no cover
'''
Contains models that store data
'''
from typing import List
from pydantic import BaseModel
from . import specialistmodel, notemodel, appointmentmodel, medicationmodel

class Patient(BaseModel): # pragma: no cover
    '''
    Class for the patients.

    Attributes:
        Id (Int): id of the patient
        FirstName (String): first name of the patient
        LastName (String): last name of the patient
        EMail (String): email of the patient
        Age (Int): age of the patient
        PhoneNumber (String): phonenumber of the patient
        Gender (Bool): gender of patient --> True male, False female
        FirstNameContact (String): first name of the contact person
        LastNameContact (String): last name of the contact person
        EMailContact (String): email of the contact person
        PhoneNumberContact (String): phonenumber of the contact person
        Specialist (List[Specialist]): List of specialisten the patient sees
        Notes (List[Note]): List of notes made by specialist about the patient
        Medications (List[Medication]): List of medication the patient has
        Appointments (List[Appointment]): List of appointments the patient has
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
    Specialists: List[specialistmodel.Specialist]
    Notes: List[notemodel.Note]
    Medications: List[medicationmodel.Medication]
    Appointments: List[appointmentmodel.Appointment]
