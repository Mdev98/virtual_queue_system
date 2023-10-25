import re
import hashlib

def validate_name(name:str):
    # Validate name as a string
    if not isinstance(name, str):
        return False
    return True
    

def validate_email(email:str):
     # Validate email using a simple regex pattern
    email_pattern = r'^\S+@\S+\.\S+$'
    if not re.match(email_pattern, email):
        return False
    return True
    
def validate_password(password:str):
    # Validate password using regex
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=])([A-Za-z\d@#$%^&+=]){8,16}$'
    if not re.match(password_pattern, password):
        return False
    return True
    
def validate_confirm_passsword(password:str, confirm_password:str):
    # Check if password and confirm_password match
    if password != confirm_password:
        return False   
    return True

def hash_password(password:str, salt:str) -> bytes:
    salt_to_byte = salt.encode('utf-8')

    # Hash the password with the salt
    password_bytes = password.encode('utf-8')
    password_hash = hashlib.pbkdf2_hmac('sha256', password_bytes, salt_to_byte, 100000)

    # Return the salt and the hashed password as bytes
    return password_hash

def verify_password(provided_password, stored_salt, stored_hashed_password) -> bool:
    # Hash the provided password using the stored salt
    password_bytes = provided_password.encode('utf-8')
    hashed_password = hashlib.pbkdf2_hmac('sha256', password_bytes, stored_salt, 100000)

    # Compare the hashed password with the stored hashed password
    return hashed_password == stored_hashed_password
