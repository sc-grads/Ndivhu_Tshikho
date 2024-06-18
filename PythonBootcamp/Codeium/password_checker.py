def validate_password(password):
    """
    Validates a password based on a set of criteria.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8 or len(password) > 20:
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    
    if not any(char in '!@#$%^&*()_+{}:;"\'<>?,.~`' for char in password):
        return False
    
    return True     

def validate_password_with_error_messages(password):
    if len(password) < 8:
        raise ValueError("Password is too short. Must be at least 8 characters long.")
    if len(password) > 20:
        raise ValueError("Password is too long. Must be at most 20 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not any(char in '!@#$%^&*()_+{}:;"\'<>?,.~`' for char in password):
        raise ValueError("Password must contain at least one special character.")


import re

def validate_password_with_error_messages(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}:;"\'<>?,.~`])[A-Za-z\d!@#$%^&*()_+{}:;"\'<>?,.~`]{8,20}$')
    if not pattern.match(password):
        raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character, and be at least 8 characters long and at most 20 characters long.")
