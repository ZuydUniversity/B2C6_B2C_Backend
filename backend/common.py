'''
File with common functions used by multiple files
'''
from fastapi import APIRouter

def create_router():
    '''
    Creates a api router.
    12345678-abcd-1234-abcd-12345678abcd

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
