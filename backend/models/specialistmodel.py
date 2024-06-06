'''
Contains models that store data
'''
from typing import List
from . import usermodel

class Specialist(usermodel.User):
    '''Class for the specialists. This is an Inherits from Usermodel '''
    PatientIds: List[int]
    NoteIds: List[int]
    SessionsId: List[int]
    AppointmentsIds: List[int]
