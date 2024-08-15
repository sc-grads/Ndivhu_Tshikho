user = {"username": "jose", "access_level": "guest"}

def get_admin_pass():
    return "1234"

def make_secure(access_level):
    def decorator(func):
        if user["access_level"] == access_level:
            return func
        else:
            return "Unauthorized"
    return decorator

get_admin = make_secure("admin")

