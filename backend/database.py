import hvac
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Initialize the Vault client
client = hvac.Client(url='http://vault.myolink.info.gf:8200')

def login_with_userpass(username, password):
    #Log in to Vault using the Username (userpass) method and set the client token.
    try:
        # Authenticate with Vault using the userpass method
        login_response = client.auth.userpass.login(
            username=username,
            password=password,
            mount_point='userpass'
        )
        # Set the client token to the newly acquired token
        client.token = login_response['auth']['client_token']
        return client.token
    except Exception as e:
        print(f"Error logging in to Vault: {e}")
        return None

def read_secret(client, path, mount_point='db'):
    #Read a secret from the KV Version 2 secrets engine.
    try:
        read_response = client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=mount_point
        )
        return read_response['data']['data']  # The secret data is nested under 'data' key twice for KV V2
    except Exception as e:
        print(f"Error reading secret from Vault: {e}")
        return None

def create_database_session(database_url):
    # Create a SQLAlchemy engine and sessionmaker.
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal

def main():
    # Get the Vault login credentials from environment variables
    vault_username = os.getenv('VAULT_USERNAME')
    vault_password = os.getenv('VAULT_PASSWORD')

    if not vault_username or not vault_password:
        print("Vault username or password not set in environment variables")
        return

    # Use the function with your credentials
    token = login_with_userpass(vault_username, vault_password)
    if token:
        client.token = token
        print("Token:", client.token)
        
        secret_data = read_secret(client, path='credentials', mount_point='db')
        if secret_data:
            print("Successfully retrieved secret:", secret_data)
            username = secret_data.get('username')
            password = secret_data.get('password')
            if username and password:
                host = 'developmentvm1-klasb2c.westeurope.cloudapp.azure.com'
                port = '3306'
                database_name = 'myolinkdb'
                # Construct the DATABASE_URL for MariaDB using PyMySQL driver
                database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"
                print("DATABASE_URL:", database_url)
                
                # Create the SQLAlchemy engine and sessionmaker
                engine, SessionLocal = create_database_session(database_url)
                print("SQLAlchemy engine and sessionmaker created successfully")
                
                # Example usage of session
                session = SessionLocal()
                try:
                    # Add your database operations here
                    pass
                finally:
                    session.close()
            else:
                print("Username or password not found in secret data")
        else:
            print("Failed to retrieve secret data")
    else:
        print("Failed to authenticate to Vault")

if __name__ == "__main__":
    main()
