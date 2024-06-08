'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app
from backend.security import pwd_context, fake_users_db, create_access_token

client = TestClient(app)

# Test data
test_user = {
    "email": "test@example.com",
    "password": "testpassword"
}

fake_users_db[test_user["email"]] = {
    "email": test_user["email"],
    "password": pwd_context.hash(test_user["password"])
}

def test_login_access_token():
    '''
    Test if logging in works 
    '''
    response = client.post("/api/user/login", json=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_access_token_invalid_credentials():
    '''
    Test if you won't loggin when wrong credentials are entered
    '''
    response = client.post("api/user/login", json={"email": "wrong@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json() == {"detail", "Incorrect email or password"}

def test_get_current_user():
    '''
    Test if can get current user when logged in
    '''
    token = create_access_token(data={"sub": test_user["email"]})
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/user", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == test_user["email"]

def test_get_current_user_invalid_token():
    '''
    Test if can't get current user when not loggedin
    '''
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.post("/api/user", headers=headers)
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
