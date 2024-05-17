from fastapi import APIRouter, HTTPException
import mariadb, re
from pydantic import BaseModel
from typing import List

conn_params= {
    "user" : "databaseuser",
    "password" : "$uperVe1ligWachtWoord",
    "host" : "20.86.139.126",
    "database" : "mvp"
}

class Person(BaseModel):
    id: int
    name: str
    age: int

router = APIRouter(prefix="/people", tags=["people"], responses={404: {"description": "Not found"}, 400: {"detail": "Invalid name. Only letters are allowed."}, 500: {"detail": "Internal Server Error"}})

@router.get("/{name}", response_model=List[Person])
async def read_person(name: str) -> List[Person]:
    if not re.match("^[A-Za-z]*$", name):
        raise HTTPException(status_code=400, detail="Invalid name. Only letters are allowed.")

    # Establish a connection
    connection= mariadb.connect(**conn_params)

    cursor= connection.cursor()

    # Parameterized query to prevent SQL injection
    query = "SELECT * FROM people WHERE name LIKE ?"

    try:
        cursor.execute(query, (f"{name}%",))

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        people = []
        for person in result:
            people.append(Person(id=person[0], name=person[1], age=person[2]))

        return people

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e