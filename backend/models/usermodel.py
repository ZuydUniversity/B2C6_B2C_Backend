'''
Contains models that store data
'''
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    '''Class for the User.'''
    Id: int
    FirstName: str
    LastName: str
    Email: str
    Password: str
    PhoneNumber: str
    Settings: List[bool]
