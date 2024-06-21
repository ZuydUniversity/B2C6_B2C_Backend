'''
Entry file of fastapi project
'''
import ssl
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import homerouter, userrouter

routers = [homerouter, userrouter]

app = FastAPI()

ssl_cert = os.getenv('SSL_CERT')
ssl_key = os.getenv('SSL_KEY')

if ssl_cert is None or ssl_key is None:
    raise ValueError("SSL certificates not found in environment variables")

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for i in routers:
    app.include_router(i.router)

app.debug = True
