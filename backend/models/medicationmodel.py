'''
Contains models that store data
'''
from pydantic import BaseModel
from typing import List

class Medication(BaseModel): # pragma: no cover
    '''
    Class for the medication.
    
    Attributes:
        Id (Int): id of the medication
        Name (String): name of the medication
        Dossage (String): dossage of the medication
        PatientIds (List[Int]): List of ids of patients who have this medication
    '''
    Id: int
    Name: str
    Dossage: str
    PatientIds: List[int]
