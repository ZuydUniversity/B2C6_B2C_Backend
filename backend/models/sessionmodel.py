'''
Contains models that store data
'''
from pydantic import BaseModel

class Session(BaseModel):
    '''
    Template model, this is just a basic model
    
    attributes:
    id (int): Id of model
    name (string): Name of model
    address (string): Address of model

    '''
    id: int
    name: str
    address: str
