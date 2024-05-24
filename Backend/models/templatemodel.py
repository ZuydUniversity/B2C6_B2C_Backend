from pydantic import BaseModel

## Template model, this is just a basic model
## Make sure this is a pydantic model so FastAPI can use it as a response model.
class TemplateModel(BaseModel):
    id: int
    name: str
    address: str
