# Contacts book

import sqlite3
import os.path

# Datbase Name
db_name = "contacts.db"

#add logic to create database if not exists when program boots and create table if not continue and connect to the DB
#if os.path.isfile(f'./{db_name}'):


# Connect to database
conn = sqlite3.connect(db_name)

# Database cusror
cursor = conn.cursor()

# Create Table
cursor.execute(f""" 
CREATE TABLE contacts (
    first_name TEXT,
    last_name TEXT,
    mobile_number INTEGER,
    email TEXT
)""")

# Commit our changes
conn.commit()

# Close con 
conn.close()

