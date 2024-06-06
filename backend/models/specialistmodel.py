'''
Contains models that store data
'''
from ..Models import usermodel, patientmodel, notemodel, sessionmodel, appointmentmodel

class Specialist(usermodel.User):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    Patients: list[patientmodel.Patient]
    Notes: list[notemodel.Note]
    Sessions: list[sessionmodel.Session]
    Appointments: list[appointmentmodel.Appointment]
