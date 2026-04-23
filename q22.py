# Q22. Write a program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.

import sqlite3

# connect to database
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# INSERT
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Alok", 20))
conn.commit()
print("Data Inserted")

# UPDATE
cursor.execute("UPDATE student SET age = ? WHERE name = ?", (21, "Alok"))
conn.commit()
print("Data Updated")

# SELECT
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print("\nData in Table:")
for row in rows:
    print(row)

# DELETE
cursor.execute("DELETE FROM student WHERE name = ?", ("Alok",))
conn.commit()
print("\nData Deleted")

# close connection
conn.close()