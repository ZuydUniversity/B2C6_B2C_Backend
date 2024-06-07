'''
The router for the user which allows the user to register, login, logout and forgotpassword functionalities
'''
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt, JWTError
from ..models.usermodel import User
from ..Security import authenticate_user, create_access_token, oauth2_scheme, SECRET_KEY, ALGORITHM, fake_users_db, UserCredentials

router = APIRouter(prefix="/api", tags=["API"],
                   responses={404: {"description": "Not found"},
                   200: {"description": "OK"},
                   400: {"description": "Bad Request"},
                   500: {"description": "Internal Server Error"}})

@router.post("/user/login")
async def login_access_token(credentials: UserCredentials):
    '''
    Returns session token after user logged in
    '''
    authentication_user = authenticate_user(credentials.email, credentials.password)

    if not authentication_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-authenticate": "bearer"},)

    access_token = create_access_token(data={"sub": credentials.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/user")
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    '''
    Returns current logged in user
    '''

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception

    user = fake_users_db.get(email)
    if user is None:
        raise credentials_exception

    return user
