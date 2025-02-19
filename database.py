import os
import sqlite3

# Create database folder if it doesn't exist
if not os.path.exists('database_folder'):
    os.makedirs('database_folder')

# Connect to the SQLite database
conn = sqlite3.connect('database_folder/job_portal.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS applicant (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS application (id INTEGER PRIMARY KEY, applicant_id INTEGER, job_id INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS employer (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS job (id INTEGER PRIMARY KEY, title TEXT, description TEXT, requirements TEXT, employer INTEGER)''')
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, role TEXT)''')

# Verify the user table schema
cursor.execute('PRAGMA table_info(user)')
columns = cursor.fetchall()
for column in columns:
    print(column)

# Commit changes and close the connection
conn.commit()
conn.close()
