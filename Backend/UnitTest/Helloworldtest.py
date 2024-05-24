import requests as rq

## This is a basic test to make sure the API is working.
def test_read_item():
    response = rq.get("http://127.0.0.1:8000/api/") ## Makes the request to the API url.
    assert response.status_code == 200 ## Checks if the status code is 200.
    assert response.json() == {"true": "API is working!"} ## Checks if the reponse from the url is correct.

## A test should go outside our API and go back via the internet to check if it works.
## Then with multiple checks and verifications you can make sure your api request or methode is working.
    