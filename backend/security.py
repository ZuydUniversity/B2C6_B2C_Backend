'''
Contains functions and variables related to logging in and security
'''
import secrets
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# TEMP TEST DATABASE
fake_users_db = {
    "johndoe@example.com": {
        "personel_number": "1234567890",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("password"),
    }
}

class loginCredentials(BaseModel):
    '''
    Contains all credentials needed for logging in.

    Attributes:
        personel_number (string): personel number of the user
        email (string): email of the user
        password (string): password of the user    
    '''
    personel_number: str
    email: str
    password: str

def authenticate_user(personel_number: str, email: str, password: str):
    '''
    Checks if user exists and if the password is correct.

    Args:
        personel_number (string): the personel number of the user
        email (string): the email of the user
        password (string): the password of the user

    Returns:
        User if successfully logged in and false if not successfully
        logged in.
    '''
    user = fake_users_db.get(email)

    if not user or user["personel_number"] != personel_number:
        return False

    if not pwd_context.verify(password, user["hashed_password"]):
        return False

    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    '''
    Create a JWT access token.

    Args:
        data (dict): Data to be encoded into the token payload.
        expires_delta (timedelta, optional): Expiration time delta. Defaults to None.

    Returns:
        str: Encoded JWT access token.
    '''
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
