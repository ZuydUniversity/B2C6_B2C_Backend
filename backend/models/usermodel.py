'''
Contains models that store data
'''
from pydantic import BaseModel

class User(BaseModel):
    Id: int
    FirstName: str
    LastName: str
    Email: set
    PhoneNumber: str
    Settings: list[bool]
