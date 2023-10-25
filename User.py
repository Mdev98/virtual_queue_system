from database import DB

from utils import validate_name, validate_email, validate_confirm_passsword, validate_password, verify_password, hash_password

import os
from dotenv import load_dotenv
load_dotenv()

db = DB()
salt = os.getenv("SALT", "defaultsalt!")

class User:
    def __init__(self,db) -> None:
        self.db = db
        self.name:str = ""
        self.email:str = ""
        self.password:str | bytes = ""
        self.active = False

    def register(self, name:str, email:str, password:str, confirm_password:str):

        if not all([validate_name(name), validate_email(email), validate_password(password), validate_confirm_passsword(password, confirm_password)]):
            print("Unable to register")
            return False
        
        self.name = name
        self.email = email
        self.password = hash_password(password, salt)

        if not db.add_user(self):
            return False

        self.active = True
        return True
    

    def login(self, email:str, password:str):

        if not any([validate_email(email), validate_password(password)]):
            return "Invalid credentials"
        
        
        user = db.get_user(email)

        if not user:
            return "Invalid credentials"
        
        if not verify_password(password, salt, bytes.fromhex(user['password'])):
            return "Invalid credentials"
        
        user['active'] = True

        return user
        

