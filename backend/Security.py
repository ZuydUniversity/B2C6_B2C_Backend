from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "johndoe@example.com": {
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("password"),
    }
}

def authenticate_user(email: str, password: str):
    '''
    Checks if user exists and if the password is correct.

    Args:
        email (string): the email of the user
        password (string): the password of the user

    Returns:
        Uxser if successfully logged in and false if not successfully
        logged in.
    '''
    user = fake_users_db.get(email)

    if not user:
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
