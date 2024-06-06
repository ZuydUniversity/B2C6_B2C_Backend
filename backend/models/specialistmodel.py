'''
Contains models that store data
'''
from typing import List
from . import usermodel, patientmodel, notemodel, sessionmodel, appointmentmodel

class Specialist(usermodel.User):
    '''Class for the specialists. This is an Inherits from Usermodel '''
    Patients: List[patientmodel.Patient]
    Notes: List[notemodel.Note]
    Sessions: List[sessionmodel.Session]
    Appointments: List[appointmentmodel.Appointment]
