# xss_handling(vuln).py

def greet_user(name):
    return f"<h1>Welcome, {name}!</h1>"

print(greet_user("<script>alert('XSS')</script>"))
