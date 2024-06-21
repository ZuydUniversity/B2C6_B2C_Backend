import ssl
import os
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import homerouter, userrouter

routers = [homerouter, userrouter]

app = FastAPI()

ssl_cert_b64 = os.getenv('SSL_CERT')
ssl_key_b64 = os.getenv('SSL_KEY')

if ssl_cert_b64 is None or ssl_key_b64 is None:
    raise ValueError("SSL certificates not found in environment variables")

try:
    ssl_cert = base64.b64decode(ssl_cert_b64)
    ssl_key = base64.b64decode(ssl_key_b64)
except base64.binascii.Error as e:
    raise ValueError("Base64 decoding error:", e)

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=ssl_cert, keyfile=ssl_key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in routers:
    app.include_router(router.router)

app.debug = True
