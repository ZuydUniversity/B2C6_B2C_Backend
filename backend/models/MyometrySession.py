'''
This module contains the myometrysession model for the database.
'''
from backend.models.session import Session

class MyometrySession(Session):
    '''
    Pylint nono
    '''
    __tablename__ = "myometrysessions"
