from tinydb import TinyDB, Query

class DB:
    def __init__(self) -> None:
        self.db = TinyDB('data.json')


    def add_user(self, data):
        new_user = data.__dict__

        # Create a Query object for the User table
        User = Query()

        # Check if a user with the same email already exists
        existing_user = self.db.search(User.email == new_user['email'])

        if not existing_user:
            new_user['password'] = new_user['password'].hex()
            self.db.insert(new_user)
            print(f"User registration successful")
            return True
        else:
            print(f"User with email {new_user['email']} already exists.")
            return False

    def get_user(self, email):
        # Create a Query object for the User table
        User = Query()

        return self.db.search(User.email == email).pop()