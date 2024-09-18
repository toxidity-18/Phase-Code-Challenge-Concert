import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Read schema.sql file and execute SQL commands
with open('db/schema.sql', 'r') as file:
    schema = file.read()
    cursor.executescript(schema)

# Commit and close connection
conn.commit()
conn.close()

print("Database initialized successfully.")
