"""
Module for database connection and Vault integration.
"""

import sys
import os
import hvac
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Initialize the Vault client
client = hvac.Client(url='http://vault.myolink.info.gf:8200')

# SQLAlchemy setup
Base = declarative_base()

def login_with_userpass(username, password):
    """
    Log in to Vault using the Username (userpass) method and set the client token.

    Args:
        username (str): The Vault username.
        password (str): The Vault password.

    Returns:
        str: The client token if login is successful, None otherwise.
    """
    try:
        login_response = client.auth.userpass.login(
            username=username,
            password=password,
            mount_point='userpass'
        )
        client.token = login_response['auth']['client_token']
        return client.token
    except hvac.exceptions.VaultError as e:
        print(f"Error logging in to Vault: {e}")
        return None

def read_secret(vault_client, path, mount_point='db'):
    """
    Read a secret from the KV Version 2 secrets engine.

    Args:
        vault_client (hvac.Client): The Vault client.
        path (str): The path to the secret.
        mount_point (str): The mount point of the secrets engine.

    Returns:
        dict: The secret data if read is successful, None otherwise.
    """
    try:
        read_response = vault_client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=mount_point
        )
        return read_response['data']['data']
    except hvac.exceptions.VaultError as e:
        print(f"Error reading secret from Vault: {e}")
        return None

def create_database_session(database_url):
    """
    Create a SQLAlchemy engine and sessionmaker.

    Args:
        database_url (str): The database URL.

    Returns:
        tuple: A tuple containing the SQLAlchemy engine and sessionmaker.
    """
    print("Connecting to database with URL:", database_url)
    engine = create_engine(database_url, pool_pre_ping=True)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, session_local

def main():
    """
    Main function to authenticate to Vault, retrieve secrets, and create the database session.
    """
    vault_username = os.getenv('VAULT_USERNAME')
    vault_password = os.getenv('VAULT_PASSWORD')

    if not vault_username or not vault_password:
        print("Vault username or password not set in environment variables")
        return

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
                database_url = (
                    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"
                )
                print("DATABASE_URL:", database_url)
                
                try:
                    engine, session_local = create_database_session(database_url)
                    print("SQLAlchemy engine and sessionmaker created successfully")
                except Exception as e:
                    print(f"Error creating database session: {e}")
                    return

                try:
                    Base.metadata.create_all(engine)
                    print("Tables created successfully")
                except Exception as e:
                    print(f"Error creating tables: {e}")
                    return
            else:
                print("Username or password not found in secret data")
        else:
            print("Failed to retrieve secret data")
    else:
        print("Failed to authenticate to Vault")

if __name__ == "__main__":
    main()
