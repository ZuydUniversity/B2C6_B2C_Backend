'''
Contains models that store data
'''
from pydantic import BaseModel

class Medication(BaseModel):
    '''Class for the medication.'''
    Id: int
    Name: str
    Dossage: str
