'''
This module contains the doctersession model for the database.
'''
from backend.models.session import Session

class DoctorSession(Session):
    '''
    Pylint nono
    '''
    __tablename__ = "doctorsessions"
