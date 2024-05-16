from fastapi import FastAPI
from .routers import items, people
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(people.router)
app.include_router(items.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
