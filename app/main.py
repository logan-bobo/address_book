# Contacts book

import sqlite3
import os.path

# Datbase Name
db_name = 'contacts.db'
contacts_table = 'contacts'

# Connect to database
conn = sqlite3.connect(db_name)

# Database cusror
cursor = conn.cursor()

# Create Table
cursor.execute(f""" 
    CREATE TABLE {contacts_table} (
        contact_id INTEGER,
        first_name TEXT,
        last_name TEXT,
        mobile_number INTEGER,
        email TEXT
)""")

# Add contact
cursor.execute(f"""
    INSERT INTO {contacts_table} VALUES(
        1,
        'logan', 
        'cox',
        01234567891,
        'logan@lolz.com'
)""")

# Select contact inforamtion to the database
data = cursor.execute(f"""
    SELECT 
        contact_id,
        first_name, 
        last_name, 
        mobile_number, 
        email 
    FROM {contacts_table}
""").fetchall()

# Update a entry in the database
cursor.execute(f"""UPDATE {contacts_table} SET first_name = 'BOB' WHERE contact_id = 1  """)

# Commit our changes
conn.commit()

# Close con 
conn.close()

