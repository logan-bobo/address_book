# Contacts book

import sqlite3
from os import path

# Datbase and contacts table
db_name = 'contacts.db'
contacts_table = 'contacts'
db_path = (f"./{db_name}")

def create_contact():
    """
    Take in user data to create a contatc on the database
    """
    first_name = (input("What is their frist name?: "))
    last_name = input("What is their last name?: ")
    # Add error checking and loop so the user can only enter a valid number
    mobile_number = int(input("what is their mobile number: "))
    # Add error checking and loop so the user can only enter a valid email address
    email = input("What is their email: ")

    cursor.execute(f"""
    INSERT INTO {contacts_table} VALUES(
        '{first_name}', 
        '{last_name}',
        {mobile_number},
        '{email}'
    )""")

    conn.commit()

def list_all_contacts():

    # Select contact inforamtion to the database
    contacts = cursor.execute(f"""
        SELECT 
            *
        FROM {contacts_table}
    """).fetchall()

    for contact in contacts:
        print(f"""
        +---------+
        | Contact |
        +---------+
        First Name: {contact[0]}
        Seccond Name: {contact[1]}
        Mobule Number: {contact[2]}
        Email: {contact[3]}
        """)

def create_database():
        # Connect to database
    conn = sqlite3.connect(db_name)

    # Database cusror
    cursor = conn.cursor()

    # Create Table
    cursor.execute(f""" 
        CREATE TABLE {contacts_table} (
            first_name TEXT,
            last_name TEXT,
            mobile_number INTEGER,
            email TEXT
    )""")

    conn.commit()
    conn.close()

if not path.exists(db_path):
    create_database()

# Connect to database
conn = sqlite3.connect(db_name)

# Database cusror
cursor = conn.cursor()

# Main menue text
menue = ("""
+-------------------+------+
|     Function      | Code |
+-------------------+------+
| Create contact    |    1 |
| Update contact    |    2 |
| List contact      |    3 |
| Remove Contact    |    4 |
| List all contacts |    5 |
| Quit              |    6 |
+-------------------+------+
\n\t Please select a function code :- 
""")

active = True
while active:
    option = int(input(menue))
    if option == 1:
        create_contact()
    if option == 2:
        print("to do")
    if option == 3:
        print("to do ")
    if option == 4:
        print("to do ")
    if option == 5:
        print(list_all_contacts())


# # Update a entry in the database
# cursor.execute(f"""UPDATE {contacts_table} SET first_name = 'BOB' WHERE contact_id = 1  """)

# # Commit our changes
# conn.commit()

# # Close con 
# conn.close()

