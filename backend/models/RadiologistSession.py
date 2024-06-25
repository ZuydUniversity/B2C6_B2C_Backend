'''
This module contains the radiologistsession model for the database.
'''
from backend.models.session import Session

class RadiologistSession(Session):
    '''
    Pylint nono
    '''
    __tablename__ = "radiologistsessions"
