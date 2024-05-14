from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
