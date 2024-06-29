'''
Contains functions and variables related to logging in and security
'''
import secrets
from datetime import datetime, timedelta, timezone
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from pathlib import Path
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
RESET_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# TEMP TEST DATABASE
fake_users_db = {
    "tristanfranssen@gmail.com": {
        "personel_number": "1234567890",
        "email": "tristanfranssen@gmail.com",
        "hashed_password": pwd_context.hash("password"),
    }
}

class ForgotPasswordRequest(BaseModel):
    '''
    Contains email for password forgot request

    Attributes:
        email (string): email of user
    '''
    email: str

class ResetPasswordRequest(BaseModel):
    '''
    Contains token and new password for reset password

    Attributes:
        token (string): reset token
        new_password (string): new user password
    '''
    token: str
    new_password: str

class LoginCredentials(BaseModel):
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

def authenticate_user(credentials: LoginCredentials):
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
    user = fake_users_db.get(credentials.email)

    if not user or user["personel_number"] != credentials.personel_number:
        return False

    if not pwd_context.verify(credentials.password, user["hashed_password"]):
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

def create_reset_token(email: str):
    '''
    Creates reset token for password reset

    Args:
        email (string): email to send token to
    '''
    expire = datetime.now(timezone.utc) + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": email}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_reset_token(token: str):
    '''
    Verifies token send

    Args:
        token (string): token received
    '''
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
        return "Invalid token"

    return email

def send_reset_email(email: str, token: str):
    '''
    Sends reset email to user

    Args:
        email (string): email of user
        token (string): reset token
    '''
    reset_link = f"http://localhost:3000/reset-password?token={token}"

    html_content = ""
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / "templates/email_template.html", "r", encoding="UTF-8") as file:
        html_content = file.read()

    html_content = Template(html_content).substitute(reset_link=reset_link)

    message = MIMEMultipart("alternative")
    message["subject"] = "Password Reset Request"
    message["From"] = "myolinkportaal@gmail.com"
    message["To"] = email

    part1 = MIMEText(f"Click the link to reset your password: {reset_link}", "plain")
    part2 = MIMEText(html_content, "html")

    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()

        email_password = os.getenv('EMAIL_PASSWORD')
        server.login("myolinkportaal@gmail.com", email_password)
        server.sendmail("mail", email, message.as_string())
