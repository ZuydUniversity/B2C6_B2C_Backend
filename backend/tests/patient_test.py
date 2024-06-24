'''
This module contains the test for patient model
'''
from backend.models.patient import Patient

def test_patient_creation():
    patient = Patient(
        firstName="John",
        lastName="Doe",
        email="john.doe@example.com",
        age=30,
        phonenumber=1234567890,
        gender="Male",
        contactpersonEmail="jane.doe@example.com",
        contactpersonPhonenumber=9876543210
    )
    assert patient.firstName == "John"
    assert patient.lastName == "Doe"
    assert patient.email == "john.doe@example.com"
    assert patient.age == 30
    assert patient.phonenumber == 1234567890
    assert patient.gender == "Male"
    assert patient.contactpersonEmail == "jane.doe@example.com"
    assert patient.contactpersonPhonenumber == 9876543210
    