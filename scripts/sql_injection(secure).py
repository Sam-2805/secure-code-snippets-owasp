# sql_injection_secure.py

import sqlite3

def get_user(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = ?"
    cursor.execute(query, (name,))
    print(cursor.fetchall())
    conn.close()

get_user("admin' --")
