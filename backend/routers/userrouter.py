'''
The router for the user which allows the user to register, 
login, logout and forgotpassword functionalities
'''
from typing import Optional
from fastapi import Depends, Response, HTTPException, status, Cookie
from fastapi.security import OAuth2PasswordRequestForm
from ..security import authenticate_user, create_access_token
from ..common import create_router

router = create_router()

@router.post("/user/login")
async def login(response: Response, credentials: OAuth2PasswordRequestForm = Depends()):
    '''
    Returns session token after user logged in
    '''
    authentication_user = authenticate_user(credentials.username, credentials.password)

    if not authentication_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-authenticate": "bearer"},)

    access_token = create_access_token(data={"sub": credentials.username})
    response.set_cookie(key="session_token", value=access_token, httponly=True, max_age=1800)

    return {"message": "Successfully logged in"}

@router.post("/user/logout")
async def logout(response: Response, session_token: Optional[str] = Cookie(None)):
    '''
    Logs out user from current session
    '''
    if session_token:
        response.delete_cookie(key="session_token")

    return {"message": "Logged out"}
