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

# Decode base64 strings to binary
ssl_cert = os.getenv('SSL_CERT')
ssl_key = os.getenv('SSL_KEY')

# Create SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

# Write the decoded certificates to temporary files
with open('/tmp/cert.pem', 'w') as f_cert, open('/tmp/key.pem', 'w') as f_key:
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
