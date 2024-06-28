"""
Module for database connection without Vault integration.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

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
    load_dotenv()
    # Constructing the database URL
    db_url = os.getenv('DB_URL')
    print(db_url)


    ## These are the tables that you must create in the database, Here you don't lay relations.
    ## The relations with foreign keys are made later.
    metadata = MetaData()

    patients = Table('patients', metadata,
        Column('id', Integer, primary_key=True),
        # other columns for the Patients table
    )

    sessions = Table('sessions', metadata,
        Column('id', Integer, primary_key=True),
        # other columns for the Sessions table
    )

    notes = Table('notes', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('description', String(200)),
        Column('specialist_id', Integer, ForeignKey('specialists.id')),
        Column('patient_id', Integer, ForeignKey('patients.id')),
        Column('session_id', Integer, ForeignKey('sessions.id')),
    )

    if db_url:
        database_url = db_url
    else:
        # Replace db_user and db_password with your actual values
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        if not db_user or not db_password:
            print("Database credentials not set in environment variables")
            return None, None
        
        database_url = f"mysql+pymysql://{db_user}:{db_password}@developmentvm1-klasb2c.westeurope.cloudapp.azure.com:3306/myolinkdb"
    
    try:
        engine, session_local = create_database_session(database_url)
        print("SQLAlchemy engine and sessionmaker created successfully")
        ## At this line the code fucks it self, It's because foreign keys point to eachother.
        ## To fix it you need to define the table first then create them, then after you can create the foreign keys.
        Base.metadata.create_all(engine) # this creates the tables
        print("Database tables created successfully")
        engine.dispose()
        print("SQLAlchemy engine and sessionmaker disposed successfully")
    except Exception as e:
        print(f"Error creating database session: {e}")

        
    # Manually create foreign key constraints after creating all the tables
    notes.c.patient_id.create(
        ForeignKey('patients.id', deferrable=True, initially='DEFERRED')
    )

    notes.c.session_id.create(
        ForeignKey('sessions.id', deferrable=True, initially='DEFERRED')
    )


def main():
    """
    Main function to run when the script is executed directly.
    """
    setup_database_connection()

if __name__ == "__main__":
    main()
