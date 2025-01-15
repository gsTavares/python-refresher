import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}."
        return secure_function
    return decorator

@make_secure("admin")
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
    
@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(get_password("billing"))
print(get_dashboard_password())