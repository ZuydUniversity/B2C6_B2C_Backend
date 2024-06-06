'''
Contains models that store data
'''
from pydantic import BaseModel

class Medication(BaseModel):
    Id: int
    Name: str
    Dossage: str
