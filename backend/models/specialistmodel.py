'''
Contains models that store data
'''
from Backend.Models import usermodel, patientmodel, notemodel, sessionmodel, appointmentmodel

class Specialist(usermodel.User):
    '''Class for the specialists. This is an Inherits from Usermodel'''
    Patients: list[patientmodel.Patient]
    Notes: list[notemodel.Note]
    Sessions: list[sessionmodel.Session]
    Appointments: list[appointmentmodel.Appointment]
