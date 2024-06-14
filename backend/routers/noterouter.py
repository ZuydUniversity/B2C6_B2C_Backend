'''
The router for the user which allows the user to register, 
login, logout and forgotpassword functionalities
'''
from ..common import create_router

router = create_router()

@router.post("/notes/create")
async def create_note():
    '''
    Creates a note
    '''
    pass