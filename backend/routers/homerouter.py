'''
Countains home router for api
'''
from fastapi import APIRouter
from ..common import create_router

router = create_router()

@router.get("/")
async def homeurl():
    '''
    For checking if router works

    return:
        Map (bool, string): Api is working

    '''
    return { True : "API is working!"}
