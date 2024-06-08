'''
File with common functions used by multiple files
'''
from fastapi import APIRouter

def create_router():
    '''
    Creates a api router.

    Return:
        returns new APIRouter.
    '''
    return APIRouter(prefix="/api", tags=["API"],
                     responses={
                         404: {"description": "Not found"},
                         200: {"description": "OK"},
                         400: {"description": "Bad Request"},
                         500: {"description": "Internal Server Error"}
                     })
