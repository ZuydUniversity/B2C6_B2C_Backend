"""
Module for testing database connection.
"""

import os
import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from backend import database  # Adjust the import path to match your project structure

class TestDatabase(unittest.TestCase):
    """
    Test case for the database module.
    """

    @patch('backend.database.create_engine')
    @patch('backend.database.sessionmaker')
    def test_create_database_session(self, mock_sessionmaker, mock_create_engine):
        """
        Test successful database session creation.
        """
        database_url = "sqlite:///:memory:"
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_sessionmaker.return_value = mock_session

        engine, session_local = database.create_database_session(database_url)

        mock_create_engine.assert_called_once_with(database_url, pool_pre_ping=True)
        mock_sessionmaker.assert_called_once_with(autocommit=False, autoflush=False, bind=mock_engine)
        self.assertEqual(engine, mock_engine)
        self.assertEqual(session_local, mock_session)

    @patch.dict(os.environ, {"DB_USER": "test_user", "DB_PASSWORD": "test_password"})
    @patch('backend.database.create_database_session')
    def test_setup_database_connection_success(self, mock_create_database_session):
        """
        Test setup database connection with valid environment variables.
        """
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_create_database_session.return_value = (mock_engine, mock_session)

        engine, session_local = database.setup_database_connection()

        mock_create_database_session.assert_called_once()
        self.assertEqual(engine, mock_engine)
        self.assertEqual(session_local, mock_session)

    @patch.dict(os.environ, {"DB_USER": "", "DB_PASSWORD": ""})
    def test_setup_database_connection_missing_credentials(self):
        """
        Test setup database connection with missing credentials.
        """
        engine, session_local = database.setup_database_connection()
        self.assertIsNone(engine)
        self.assertIsNone(session_local)

    @patch.dict(os.environ, {"DB_USER": "test_user", "DB_PASSWORD": "test_password"})
    @patch('backend.database.create_database_session', side_effect=SQLAlchemyError("Connection failed"))
    def test_setup_database_connection_exception(self, mock_create_database_session):
        """
        Test setup database connection with an exception during session creation.
        """
        engine, session_local = database.setup_database_connection()

        mock_create_database_session.assert_called_once()
        self.assertIsNone(engine)
        self.assertIsNone(session_local)

if __name__ == "__main__":
    unittest.main()
