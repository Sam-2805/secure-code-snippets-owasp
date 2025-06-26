# sql_injection.py (vulnerable version)

import sqlite3

def get_user(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    print(cursor.fetchall())
    conn.close()

get_user("admin' --")


