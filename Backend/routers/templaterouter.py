from fastapi import APIRouter

## Make sure to import your model, otherwise you will get an error that your model is not found.
from ..models.templatemodel import TemplateModel

## Prefix is to make the path, make sure API is always at the beginning of this.
## The responses are premade for you to use. I recommend to don't toutch when you don't know what you are doing.
router = APIRouter(prefix="/api/template", tags=["template"],responses={404: {"description": "Not found"}, 200: {"description": "OK"}, 400: {"description": "Bad Request"}, 500: {"description": "Internal Server Error"}})


## Basic get request.
## Don't forget to change the response_model to your model so the changes reflect properly inside the interactive docs.
@router.get("/",  response_model=TemplateModel)
async def get_template():
    models = TemplateModel(id=1, name="Homoerectus", address="USA")
    return models
