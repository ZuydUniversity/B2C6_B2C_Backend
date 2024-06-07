'''
Contains models that store data
'''
from typing import List
from . import usermodel

class Specialist(usermodel.User):
    '''
    Class for the specialists. This is an Inherits from Usermodel
    
    Attributes:
        PatientIds (List[Int]): list of the ids of the specialists patients 
        NoteIds (List[Int]): list of ids of the notes made by specialist 
        SessionIds (List[Int]): List of ids of sessions in which the specialist partakes
        AppointmentIds (List[Int]): List of ids of appointments in which the specialist partakes
    '''
    PatientIds: List[int]
    NoteIds: List[int]
    SessionIds: List[int]
    AppointmentIds: List[int]
