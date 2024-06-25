'''
This module contains the User model for the database.
'''
from sqlalchemy import Column, Integer, String
from backend.database import Base

class User(Base):
    '''
    This is a parent class.
    '''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    password = Column(String(50))
    email = Column(String(100), unique=True)
    phonenumber = Column(Integer, unique=True)
    settings = Column(String(100))
