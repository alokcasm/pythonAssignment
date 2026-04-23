# Q21. Write a program to connect to a database and create a table.


import sqlite3

# connect to database (creates file if not exists)
conn = sqlite3.connect("mydb.db")

# create cursor object
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

print("Table created successfully")

# close connection
conn.close()