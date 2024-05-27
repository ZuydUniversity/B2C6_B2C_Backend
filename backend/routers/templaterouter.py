'''
Contains router for template api
'''
from fastapi import APIRouter
from ..models.templatemodel import TemplateModel

router = APIRouter(prefix="/api/template",
                   tags=["template"],
                   responses={404: {"description": "Not found"},
                   200: {"description": "OK"},
                   400: {"description": "Bad Request"},
                   500: {"description": "Internal Server Error"}})

@router.get("/",  response_model=TemplateModel)
async def get_template():
    '''
    Basic request funtion. Change TemplateModel with your model.
    '''
    models = TemplateModel(id=1, name="Homoerectus", address="USA")
    return models