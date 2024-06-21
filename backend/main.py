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

# Save decoded certificates to temporary files
cert_file_path = "/tmp/cert.pem"
key_file_path = "/tmp/key.pem"

with open(cert_file_path, "wb") as cert_file:
    cert_file.write(ssl_cert)

with open(key_file_path, "wb") as key_file:
    key_file.write(ssl_key)

# Load certificates into SSL context
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=cert_file_path, keyfile=key_file_path)

# Clean up temporary files
os.remove(cert_file_path)
os.remove(key_file_path)

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
