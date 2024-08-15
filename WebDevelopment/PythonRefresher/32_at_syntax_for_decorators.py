user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "1234"

@make_secure("user")
def get_user_password():
    return "user_password"

print(get_admin_password())
print(get_user_password())
