# setup_db.py

import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert some dummy users
cursor.executemany('''
INSERT INTO users (name, email) VALUES (?, ?)
''', [
    ('admin', 'admin@example.com'),
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com')
])

conn.commit()
conn.close()

print("users.db created and populated.")
