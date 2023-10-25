import unittest
import tempfile
from User import User
from tinydb import TinyDB


class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory to hold the database file
        self.temp_dir = tempfile.TemporaryDirectory()

        # Define the path for the temporary database file
        temp_db_path = self.temp_dir.name + '/temp_db.json'

        # Create a TinyDB instance with the temporary database file
        self.db = TinyDB(temp_db_path)

    def tearDown(self):
        # Clean up the temporary directory and the database file
        self.db.drop_tables()

    def test_register_valid_user(self):
        user = User(self.db)
        result = user.register("JohnDoe", "johndoe@example.com", "Test1234+", "Test1234+")
        self.assertTrue(result)  # Check that registration was successful
        self.assertTrue(user.active)  # Check that the user is active

    def test_register_invalid_user(self):
        user = User(self.db)
        result = user.register("John Doe", "invalid_email", "Weak", "Weak")
        self.assertFalse(result)  # Check that registration failed
        self.assertFalse(user.active)  # Check that the user is not active

    def test_login_valid_user(self):
        user = User(self.db)
        user.register("John Doe", "john.doe@example.com", "Test1234+", "Test1234+")
        result = user.login("john.doe@example.com", "Test1234+")
        self.assertIsInstance(result, dict)  # Check that a valid user dictionary is returned

    def test_login_invalid_credentials(self):
        user = User(self.db)
        result = user.login("nonexistent@example.com", "InvalidPassword")
        self.assertEqual(result, "Invalid credentials")  # Check that login failed due to invalid credentials

if __name__ == '__main__':
    unittest.main()
