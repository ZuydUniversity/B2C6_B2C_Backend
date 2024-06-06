'''
Contains models that store data
'''
from pydantic import BaseModel

class User(BaseModel):
    '''Class for the User.'''
    Id: int
    FirstName: str
    LastName: str
    Email: set
    PhoneNumber: str
    Settings: list[bool]
