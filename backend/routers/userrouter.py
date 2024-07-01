'''
The router for the user which allows the user to register, 
login, logout and forgotpassword functionalities
'''
from typing import Optional
from fastapi import Response, HTTPException, status, Cookie
from ..security import authenticate_user, create_access_token, LoginCredentials, ForgotPasswordRequest, fake_users_db, \
                       create_reset_token, verify_reset_token, send_reset_email, ResetPasswordRequest, pwd_context
from ..common import create_router

router = create_router()

@router.post("/user/login")
async def login(response: Response, credentials: LoginCredentials):
    '''
    Returns session token after user logged in
    '''
    authentication_user = authenticate_user(credentials)

    if not authentication_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-authenticate": "bearer"},)

    access_token = create_access_token(data={"sub": credentials.email})
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

@router.post("/user/forgot-password")
async def forgot_password(request: ForgotPasswordRequest):
    '''
    Sends a password reset email

    Args:
        request (ForgotPasswordRequest): contains data about the request
    '''
    user = fake_users_db[request.email]

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="email not found")

    reset_token = create_reset_token(request.email)
    send_reset_email(request.email, reset_token)

    return {"message": "Password reste email send"}

@router.post("/user/reset-password")
async def reset_password(request: ResetPasswordRequest):
    '''
    Resets password

    Args:
        request (ResetPasswordRequest): contians data about the request
    '''
    email = verify_reset_token(request.token)

    if email == "Invalid token":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

    fake_users_db[email]["hashed_password"] = pwd_context.hash(request.new_password)

    return {"message": "Password has been reset"}
