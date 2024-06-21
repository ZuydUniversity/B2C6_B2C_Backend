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

ssl_cert_b64 = os.getenv('SSL_CERT')
ssl_key_b64 = os.getenv('SSL_KEY')

if ssl_cert_b64 is None or ssl_key_b64 is None:
    raise ValueError("SSL certificates not found in environment variables")

# Decode base64 strings to binary
ssl_cert = base64.b64decode(ssl_cert_b64)
ssl_key = base64.b64decode(ssl_key_b64)

# Create SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

# Write the decoded certificates to temporary files
with open('/tmp/cert.pem', 'wb') as f_cert, open('/tmp/key.pem', 'wb') as f_key:
    f_cert.write(ssl_cert)
    f_key.write(ssl_key)

# Load certificates and keys from temporary files
ssl_context.load_cert_chain(certfile='/tmp/cert.pem', keyfile='/tmp/key.pem')

# Clean up temporary files (optional)
os.remove('/tmp/cert.pem')
os.remove('/tmp/key.pem')

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
