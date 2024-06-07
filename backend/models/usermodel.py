'''
Contains models that store data
'''
from typing import List
from pydantic import BaseModel

class User(BaseModel): # pragma: no cover
    '''
    Class for the User.
    
    Attributes:
        Id (Int): id of user
        FirstName (String): first name of user
        LastName (String): last name of user
        Email (String): email of user
        Password (String): hashed password of user
        PhoneNumber (String): phonenumber of user
        Settings (List[Bool]): list of settings of user
    '''
    Id: int
    FirstName: str
    LastName: str
    Email: str
    Password: str
    PhoneNumber: str
    Settings: List[bool]
