'''
Entry file of fastapi project
'''
import ssl
import os
import base64
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import homerouter, userrouter

routers = [homerouter, userrouter]

app = FastAPI()

ssl_cert = os.getenv('SSL_CERT')
ssl_key = os.getenv('SSL_KEY')

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(cert_bytes=ssl_cert, key_bytes=ssl_key)

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
