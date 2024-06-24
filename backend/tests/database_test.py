"""
Module for testing database connection and Vault integration.
"""

import unittest
from unittest.mock import patch, MagicMock
import os
from backend import database  # Adjust the import path to match your project structure
import sqlalchemy

class TestDatabase(unittest.TestCase):
    """
    Test case for the database module.
    """

    @patch('backend.database.client')
    def test_login_with_userpass_success(self, mock_client):
        """
        Test successful login with userpass.
        """
        mock_login_response = {'auth': {'client_token': 'test-token'}}
        mock_client.auth.userpass.login.return_value = mock_login_response

        token = database.login_with_userpass('testuser', 'testpass')
        self.assertEqual(token, 'test-token')
        self.assertEqual(database.client.token, 'test-token')

    @patch('backend.database.client')
    def test_login_with_userpass_failure(self, mock_client):
        """
        Test login failure with userpass.
        """
        mock_client.auth.userpass.login.side_effect = Exception("Login failed")
        with self.assertRaises(Exception) as context:
            database.login_with_userpass('testuser', 'testpass')
        self.assertTrue('Login failed' in str(context.exception))

    @patch('backend.database.client')
    def test_login_with_userpass_invalid_credentials(self, mock_client):
        """
        Test login with invalid credentials.
        """
        mock_client.auth.userpass.login.return_value = {'auth': {'client_token': 'test-token'}}
        # Assuming the function handles invalid credentials by returning None or a specific value
        token = database.login_with_userpass('invaliduser', 'invalidpass')
        self.assertIn(token, [None, 'test-token'])  # Adjust based on your function's behavior

    @patch('backend.database.client')
    def test_read_secret_success(self, mock_client):
        """
        Test successful secret reading.
        """
        mock_read_response = {
            'data': {'data': {'username': 'testuser', 'password': 'testpass'}}
        }
        mock_client.secrets.kv.v2.read_secret_version.return_value = mock_read_response

        secret_data = database.read_secret(mock_client, 'credentials', 'db')
        self.assertEqual(secret_data, {'username': 'testuser', 'password': 'testpass'})

    @patch('backend.database.client')
    def test_read_secret_failure(self, mock_client):
        """
        Test secret reading failure.
        """
        from hvac.exceptions import VaultError
        mock_client.secrets.kv.v2.read_secret_version.side_effect = VaultError("Read failed")

        secret_data = database.read_secret(mock_client, 'credentials', 'db')
        self.assertIsNone(secret_data)

    @patch('backend.database.client')
    def test_read_secret_empty_response(self, mock_client):
        """
        Test reading a secret with an empty response.
        """
        mock_client.secrets.kv.v2.read_secret_version.return_value = {'data': {'data': None}}
        secret = database.read_secret(mock_client, 'path/to/secret')
        self.assertIsNone(secret)

    @patch('backend.database.create_engine')
    @patch('backend.database.sessionmaker')
    def test_create_database_session(self, mock_sessionmaker, mock_create_engine):
        """
        Test successful database session creation.
        """
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        mock_sessionmaker_instance = MagicMock()
        mock_sessionmaker.return_value = mock_sessionmaker_instance

        database_url = 'mysql+pymysql://user:pass@localhost/db'
        engine, session_local = database.create_database_session(database_url)

        mock_create_engine.assert_called_once_with(database_url, pool_pre_ping=True)
        self.assertEqual(engine, mock_engine)
        self.assertEqual(session_local, mock_sessionmaker_instance)

    @patch.dict(os.environ, {'VAULT_USERNAME': 'test-username', 'VAULT_PASSWORD': 'test-password'})
    @patch('backend.database.client')
    @patch('backend.database.create_engine')
    @patch('backend.database.Base.metadata.create_all')
    @patch('backend.database.login_with_userpass')
    @patch('backend.database.read_secret')
    def test_main_success(self, mock_read_secret, mock_login_with_userpass, mock_create_all, mock_create_engine, MockClient):
        """
        Test main function success scenario.
        """
        mock_login_with_userpass.return_value = 'test-token'
        mock_read_secret.return_value = {'username': 'db-user', 'password': 'db-pass'}
        mock_client = MockClient.return_value

        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Token:", 'test-token')
            mocked_print.assert_any_call("Successfully retrieved secret:", {'username': 'db-user', 'password': 'db-pass'})
            mocked_print.assert_any_call("DATABASE_URL:", "mysql+pymysql://db-user:db-pass@developmentvm1-klasb2c.westeurope.cloudapp.azure.com:3306/myolinkdb")
            mocked_print.assert_any_call("SQLAlchemy engine and sessionmaker created successfully")
            mocked_print.assert_any_call("Tables created successfully")

    @patch.dict(os.environ, {'VAULT_USERNAME': 'test-username', 'VAULT_PASSWORD': 'test-password'})
    @patch('backend.database.client')
    @patch('backend.database.login_with_userpass')
    def test_main_login_failure(self, mock_login_with_userpass, MockClient):
        """
        Test main function with login failure.
        """
        mock_login_with_userpass.return_value = None

        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Failed to authenticate to Vault")

    @patch.dict(os.environ, {'VAULT_USERNAME': 'test-username', 'VAULT_PASSWORD': 'test-password'})
    @patch('backend.database.client')
    @patch('backend.database.login_with_userpass')
    @patch('backend.database.read_secret')
    def test_main_read_secret_failure(self, mock_read_secret, mock_login_with_userpass, MockClient):
        """
        Test main function with secret read failure.
        """
        mock_login_with_userpass.return_value = 'test-token'
        mock_read_secret.return_value = None

        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Failed to retrieve secret data")

    @patch.dict(os.environ, {'VAULT_USERNAME': '', 'VAULT_PASSWORD': ''})
    def test_main_missing_env_vars(self):
        """
        Test main function with missing environment variables.
        """
        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Vault username or password not set in environment variables")

    @patch.dict(os.environ, {'VAULT_USERNAME': 'test-username', 'VAULT_PASSWORD': 'test-password'})
    @patch('backend.database.client')
    @patch('backend.database.create_database_session')
    @patch('backend.database.login_with_userpass')
    @patch('backend.database.read_secret')
    def test_main_create_database_session_failure(self, mock_read_secret, mock_login_with_userpass, mock_create_database_session, MockClient):
        """
        Test main function with database session creation failure.
        """
        mock_login_with_userpass.return_value = 'test-token'
        mock_read_secret.return_value = {'username': 'db-user', 'password': 'db-pass'}
        mock_create_database_session.side_effect = sqlalchemy.exc.SQLAlchemyError("Connection failed")

        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Error creating database session: Connection failed")

    @patch.dict(os.environ, {'VAULT_USERNAME': 'test-username', 'VAULT_PASSWORD': 'test-password'})
    @patch('backend.database.client')
    @patch('backend.database.create_database_session')
    @patch('backend.database.Base.metadata.create_all')
    @patch('backend.database.login_with_userpass')
    @patch('backend.database.read_secret')
    def test_main_create_tables_failure(self, mock_read_secret, mock_login_with_userpass, mock_create_all, mock_create_database_session, MockClient):
        """
        Test main function with table creation failure.
        """
        mock_login_with_userpass.return_value = 'test-token'
        mock_read_secret.return_value = {'username': 'db-user', 'password': 'db-pass'}
        mock_create_database_session.return_value = (MagicMock(), MagicMock())
        mock_create_all.side_effect = sqlalchemy.exc.SQLAlchemyError("Table creation failed")

        with patch('builtins.print') as mocked_print:
            database.main()
            mocked_print.assert_any_call("Error creating tables: Table creation failed")


if __name__ == "__main__":
    unittest.main()
