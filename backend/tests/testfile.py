'''
test
'''
from fastapi.testclient import TestClient
#import requests as rq
from backend.main import app

client = TestClient(app)

async def test():
    '''
    test
    '''
    response = client.get("https://google.com")
    assert response.status_code == 200
