'''
test
'''

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

async def test():
    '''
    test
    '''
    response = client.get("https://google.com")
    assert response.status_code == 200
