# xss_handling(secure).py

import html

def greet_user(name):
    safe_name = html.escape(name)
    return f"<h1>Welcome, {safe_name}!</h1>"

print(greet_user("<script>alert('XSS')</script>"))
