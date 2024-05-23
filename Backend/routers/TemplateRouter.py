from fastapi import APIRouter, HTTPException
import mariadb, re, os
from pydantic import BaseModel
from typing import List


router = APIRouter(prefix="/api", tags=["API"], responses={404: {"description": "Not found"}, 400: {"detail": "Invalid name. Only letters are allowed."}, 500: {"detail": "Internal Server Error"}})

@app.get("/")
async def read_root():
    return "Hello World!"