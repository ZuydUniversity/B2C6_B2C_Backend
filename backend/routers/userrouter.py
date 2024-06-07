'''
The router for the user which allows the user to register, login, logout and forgotpassword functionalities
'''
from fastapi import APIRouter, HTTPException, status
from ..models.usermodel import User
from ..Security import authenticate_user, create_access_token

router = APIRouter(prefix="/api", tags=["API"],
                   responses={404: {"description": "Not found"},
                   200: {"description": "OK"},
                   400: {"description": "Bad Request"},
                   500: {"description": "Internal Server Error"}})

@router.post("/login")
async def login_access_token(user: User):
    '''
    Returns session token after user logged in
    '''
    authentication_user = authenticate_user(user.Email, user.Password)

    if not authentication_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-authenticate": "bearer"},)

    access_token = create_access_token(data={"sub": user.Email})
    return {"access_token": access_token, "token_type": "bearer"}