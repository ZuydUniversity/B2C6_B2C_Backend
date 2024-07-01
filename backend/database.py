"""
Module for database connection without Vault integration.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKeyConstraint, ForeignKey

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
    iscreated = False

    patients = Table('patients', metadata,
        Column('id', Integer, primary_key=True),
    )

    sessions = Table('sessions', metadata,
        Column('id', Integer, primary_key=True),
        # other columns for the Sessions table
    )

    specialists = Table('specialists', metadata,
        Column('id', Integer, primary_key=True),
        # other columns for the Specialists table
    )

    notes = Table('notes', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('description', String(200)),
        Column('specialist_id', Integer),
        Column('patient_id', Integer),
        Column('session_id', Integer),
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
        Base.metadata.create_all(engine) # this creates the tables
        iscreated = True
        print("Database tables created successfully")
        
        engine.dispose()
        print("SQLAlchemy engine and sessionmaker disposed successfully")
    except Exception as e:
        print(f"Error creating database session: {e}")

    if iscreated is True:
        notes_fk_specialist = ForeignKeyConstraint(['specialist_id'], ['specialists.id'], deferrable=True, initially='DEFERRED')
        notes_fk_patient = ForeignKeyConstraint(['patient_id'], ['patients.id'], deferrable=True, initially='DEFERRED')
        notes_fk_session = ForeignKeyConstraint(['session_id'], ['sessions.id'], deferrable=True, initially='DEFERRED')

        notes.append_constraint(notes_fk_specialist)
        notes.append_constraint(notes_fk_patient)
        notes.append_constraint(notes_fk_session)
        print("Foreign keys added successfully")


def main():
    """
    Main function to run when the script is executed directly.
    """
    setup_database_connection()

if __name__ == "__main__":
    main()
