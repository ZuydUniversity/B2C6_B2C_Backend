'''
Entry file of fastapi project
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import homerouter, userrouter

routers = [homerouter, userrouter]

app = FastAPI()

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
