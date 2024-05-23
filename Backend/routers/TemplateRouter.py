from fastapi import APIRouter, Response
from Models.TemplateModel import TemplateModel

## Prefix is to make the path, make sure API is always at the beginning of this.
## The responses are premade for you to use. I recommend to don't toutch when you don't know what you are doing.
router = APIRouter(prefix="/api/template", tags=["template"],responses={404: {"description": "Not found"}, 200: {"description": "OK"}, 400: {"description": "Bad Request"}, 500: {"description": "Internal Server Error"}})


## Basic get request.
@router.get("/")
async def get_template():
    models = ["Models is working"]
    return models