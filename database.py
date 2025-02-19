import os
import sqlite3

if not os.path.exists('database_folder'):
    os.makedirs('database_folder')

conn = sqlite3.connect('database_folder/job_portal.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS applicant (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS application (id INTEGER PRIMARY KEY, applicant_id INTEGER, job_id INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS employer (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS job (id INTEGER PRIMARY KEY, title TEXT, description TEXT, requirements TEXT, employer INTEGER)''')
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, role TEXT)''')

cursor.execute('PRAGMA table_info(user)')
columns = cursor.fetchall()
for column in columns:
    print(column)

conn.commit()
conn.close()
