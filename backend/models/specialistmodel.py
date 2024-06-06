'''
Contains models that store data
'''
from typing import List
from . import usermodel, notemodel, sessionmodel, appointmentmodel

class Specialist(usermodel.User):
    '''Class for the specialists. This is an Inherits from Usermodel '''
    PatientIds: List[int]
    Notes: List[notemodel.Note]
    Sessions: List[sessionmodel.Session]
    Appointments: List[appointmentmodel.Appointment]
    