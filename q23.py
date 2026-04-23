# Q23. Demonstratetransaction control (commit and rollback) in database operations.

import sqlite3

# connect to database
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS account (
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
)
""")

# insert initial data
cursor.execute("INSERT INTO account (name, balance) VALUES (?, ?)", ("Alok", 1000))
conn.commit()

try:
    # transaction start
    cursor.execute("UPDATE account SET balance = balance - 500 WHERE name = ?", ("Alok",))
    
    # force an error (for demo)
    x = 10 / 0  

    cursor.execute("UPDATE account SET balance = balance + 500 WHERE name = ?", ("Alok",))
    
    # commit changes
    conn.commit()
    print("Transaction successful")

except:
    # rollback if error occurs
    conn.rollback()
    print("Transaction failed, changes rolled back")

# check final data
cursor.execute("SELECT * FROM account")
print("\nFinal Data:")
for row in cursor.fetchall():
    print(row)

# close connection
conn.close()