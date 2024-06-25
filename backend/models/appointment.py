'''
This module contains the Appointment model for the database.
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from backend.database import Base

class Appointment(Base):
    '''
    The Appointment model for the database.
    '''
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    