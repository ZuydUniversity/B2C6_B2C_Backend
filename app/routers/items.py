from fastapi import APIRouter

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
    "test": {"id": "test", "title": "Test", "description": "This is a test"},
}

router = APIRouter(prefix="/items", tags=["items"],responses={404: {"description": "Not found"}})

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_db:
        return {"message": "Item not found"}
    return fake_db[item_id]