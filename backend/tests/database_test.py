import unittest
from unittest.mock import patch, MagicMock
from backend import database  # Adjust the import path to match your project structure

class TestDatabase(unittest.TestCase):

    @patch('backend.database.client')
    def test_login_with_userpass_success(self, mock_client):
        mock_login_response = {'auth': {'client_token': 'test-token'}}
        mock_client.auth.userpass.login.return_value = mock_login_response

        token = database.login_with_userpass('testuser', 'testpass')
        self.assertEqual(token, 'test-token')
        self.assertEqual(database.client.token, 'test-token')

    @patch('backend.database.client')
    def test_login_with_userpass_failure(self, mock_client):
        mock_client.auth.userpass.login.side_effect = Exception("Login failed")

        token = database.login_with_userpass('testuser', 'testpass')
        self.assertIsNone(token)

    @patch('backend.database.client')
    def test_read_secret_success(self, mock_client):
        mock_read_response = {'data': {'data': {'username': 'testuser', 'password': 'testpass'}}}
        mock_client.secrets.kv.v2.read_secret_version.return_value = mock_read_response

        secret_data = database.read_secret(mock_client, 'credentials', 'db')
        self.assertEqual(secret_data, {'username': 'testuser', 'password': 'testpass'})

    @patch('backend.database.client')
    def test_read_secret_failure(self, mock_client):
        mock_client.secrets.kv.v2.read_secret_version.side_effect = Exception("Read failed")

        secret_data = database.read_secret(mock_client, 'credentials', 'db')
        self.assertIsNone(secret_data)

    @patch('backend.database.create_engine')
    @patch('backend.database.sessionmaker')
    def test_create_database_session(self, mock_sessionmaker, mock_create_engine):
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        mock_sessionmaker_instance = MagicMock()
        mock_sessionmaker.return_value = mock_sessionmaker_instance

        database_url = 'mysql+pymysql://user:pass@localhost/db'
        engine, SessionLocal = database.create_database_session(database_url)

        mock_create_engine.assert_called_once_with(database_url)
        self.assertEqual(engine, mock_engine)
        self.assertEqual(SessionLocal, mock_sessionmaker_instance)

    @patch('backend.database.client')
    def test_read_secret(self, mock_client):
        # Mock response structure from Vault's KV Version 2 secrets engine
        mock_response = {
            'data': {
                'data': {
                    'username': 'testuser2',  # Different username for this test
                    'password': 'testpass2'   # Different password for this test
                }
            }
        }
        mock_client.secrets.kv.v2.read_secret_version.return_value = mock_response

        # Expected secret data to be returned by read_secret
        expected_secret_data = {'username': 'testuser2', 'password': 'testpass2'}

        # Call the function with the mock client
        secret_data = database.read_secret(mock_client, 'path/to/secret')

        # Assert the returned secret data matches the expected data
        self.assertEqual(secret_data, expected_secret_data)

if __name__ == "__main__":
    unittest.main()
