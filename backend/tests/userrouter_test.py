'''
Test for user router
'''
from fastapi.testclient import TestClient
from backend.main import app
from backend.security import pwd_context, fake_users_db, create_reset_token

client = TestClient(app)

# Test data
test_user = {
    "personel_number": "1234567890",
    "email": "test@example.com",
    "password": "testpassword"
}

fake_users_db[test_user["email"]] = {
    "personel_number": test_user["personel_number"],
    "email": test_user["email"],
    "hashed_password": pwd_context.hash(test_user["password"])
}

def test_login_successful():
    '''
    Test if logging in works 
    '''
    response = client.post("/api/user/login", json=test_user)

    assert response.status_code == 200
    assert "session_token" in response.cookies
    assert response.json() == {"message": "Successfully logged in"}

def test_login_incorrect_credentials():
    '''
    Test if you won't loggin when wrong credentials are entered
    '''
    response = client.post("api/user/login", json={
        "personel_number": "1342341245", 
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

def test_password_reset():
    '''
    Test if you can reset a password
    '''
    reset_token = create_reset_token("johndoe@example.com")
    response = client.post("/api/user/reset-password", json={"token": reset_token, "new_password": "P@$$w0rD"})

    assert response.status_code == 200
    assert response.json() ==  {"message": "Password has been reset"}

def test_password_invalid_token_reset():
    '''
    Test if you can't reset password with invalid token
    '''
    response = client.post("/api/user/reset-password", json={"token": "123", "new_password": "P@$$w0rD"})
    assert response.status_code == 403
