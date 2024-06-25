"""
Module for database connection without Vault integration.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy setup
Base = declarative_base()

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

def setup_database_connection():
    """
    Set up the database connection by retrieving secrets from environment variables
    and creating the database session.
    """
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    if not db_user or not db_password:
        print("Database credentials not set in environment variables")
        return None, None

    # Constructing the database URL
    database_url = f"mysql+pymysql://{db_user}:{db_password}@developmentvm1-klasb2c.westeurope.cloudapp.azure.com:3306/myolinkdb"

    try:
        engine, session_local = create_database_session(database_url)
        print("SQLAlchemy engine and sessionmaker created successfully")

        try:
            Base.metadata.create_all(engine)
            print("Tables created successfully")
            return engine, session_local
        except Exception as e:
            print(f"Error creating tables: {e}")
            return None, None
    except Exception as e:
        print(f"Error creating database session: {e}")
        return None, None

def main():
    """
    Main function to run when the script is executed directly.
    """
    setup_database_connection()

if __name__ == "__main__":
    main()
