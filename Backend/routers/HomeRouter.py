from fastapi import APIRouter

## DONT TOUTCH
router = APIRouter(prefix="/api", tags=["API"],responses={404: {"description": "Not found"}, 200: {"description": "OK"}, 400: {"description": "Bad Request"}, 500: {"description": "Internal Server Error"}})

## DONT TOUTCH
@router.get("/")
async def homeurl():
    return { True : "API is working!"}