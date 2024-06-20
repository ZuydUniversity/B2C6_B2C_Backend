'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app
from backend.security import pwd_context, fake_users_db, create_access_token

client = TestClient(app)

# Test data
test_user = {
    "username": "test@example.com",
    "password": "testpassword"
}

fake_users_db[test_user["email"]] = {
    "email": test_user["email"],
    "hashed_password": pwd_context.hash(test_user["password"])
}

def test_login_successful():
    '''
    Test if logging in works 
    '''
    response = client.post("/api/user/login", data=test_user)

    assert response.status_code == 200
    assert "access_token" in response.cookies
    assert response.json() == {"message": "Successfully logged in"}

def test_login_incorrect_credentials():
    '''
    Test if you won't loggin when wrong credentials are entered
    '''
    response = client.post("api/user/login", data={
        "email": "wrong@example.com",
        "password": "wrongpassword"
    })
    
    assert response.status_code == 401
    assert "session_token" not in response.cookies
    assert response.json() == {"detail": "Incorrect email or password"}

def test_login_missing_credentials():
    '''
    Test login without credentials
    '''
    response = client.post("/api/user/login")
    
    assert response.status_code == 422
    assert "session_token" not in response.cookies

def test_logout():
    '''
    Test if you logout when logged in
    '''
    client.post("/api/user/login", json=test_user)
    response = client.post("/api/user/logout")
    assert response.status_code == 200
    assert response.json() == {"message": "Logged out"}

def test_logout_invalid_token():
    '''
    Test if can't logout when not loggedin
    '''
    response = client.post("/api/user/logout")
    assert response.status_code == 404

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
