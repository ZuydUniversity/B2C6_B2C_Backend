'''
Contains models that store data
'''
from pydantic import BaseModel

class User(BaseModel):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    Id: int
    FirstName: str
    LastName: str
    Email: set
    PhoneNumber: str
    Settings: list[bool]
