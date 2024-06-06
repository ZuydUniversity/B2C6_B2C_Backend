'''
Contains models that store data
'''
from ..Models import usermodel, patientmodel, notemodel, sessionmodel, appointmentmodel

class Specialist(usermodel.User):
    Patients: list[patientmodel.Patient]
    Notes: list[notemodel.Note]
    Sessions: list[sessionmodel.Session]
    Appointments: list[appointmentmodel.Appointment]
