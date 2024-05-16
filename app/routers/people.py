from fastapi import APIRouter
import mariadb
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

router = APIRouter(prefix="/people", tags=["people"],responses={404: {"description": "Not found"}})

@router.get("/{name}", response_model=List[Person])
async def read_person(name: str):
    # Establish a connection
    connection= mariadb.connect(**conn_params)

    cursor= connection.cursor()

    query = f"SELECT * FROM people WHERE name LIKE \"{name}%\""

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    people = []
    for person in result:
        people.append({"id": person[0], "name": person[1], "age": person[2]})

    return people