#!/usr/bin/env python3
import sqlite3
import phonenumbers
import re

from os import path


# Datbase and contacts table
db_name = 'contacts.db'
contacts_table = 'contacts'
db_path = (f"./{db_name}")

def create_contact():
    """
    Take in user data to create a contatc on the database
    """
    first_name = (input("What is their first name?: "))
    last_name = input("What is their last name?: ")
    correct_number = False
    correct_email = False
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Fix exceptions
    while correct_number is False:
        mobile_number = input("what is their mobile number: ")
        if phonenumbers.is_possible_number(mobile_number):
            correct_number = True

    # Fix exceptions
    while correct_email is False:
        email = input("What is their email: ")
        if(re.fullmatch(email_regex, email)):
            correct_email = True
        else:
            correct_email = False

    cursor.execute(f"""
    INSERT INTO {contacts_table} VALUES(
        '{first_name}', 
        '{last_name}',
        {mobile_number},
        '{email}'
    )""")

    conn.commit()

def list_all_contacts():
    """
    lists all contacts in the contact db
    """
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
        Second Name: {contact[1]}
        Mobile Number: {contact[2]}
        Email: {contact[3]}
        """)

def create_database():
    """
    Creates a database then a main contacts table in that database.
    """

    # Connect to database
    conn = sqlite3.connect(db_name)

    # Database cursor
    cursor = conn.cursor()

    # Create Table
    cursor.execute(f""" 
        CREATE TABLE {contacts_table} (
            first_name TEXT,
            last_name TEXT,
            mobile_number TEXT,
            email TEXT
    )""")

    conn.commit()
    conn.close()


# Main menu text
menu = ("""
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
\n\t Please select a function code : 
""")

if __name__ == "__main__":
    active = True

    # Create the main database if it does not exist
    if not path.exists(db_path):
        create_database()

    # Connect to database
    conn = sqlite3.connect(db_name)

    # Database cusror
    cursor = conn.cursor()

    while active:
        option = int(input(menu))
        if option == 1:
            create_contact()
        if option == 2:
            print("to do")
        if option == 3:
            print("to do ")
        if option == 4:
            print("to do ")
        if option == 5:
            list_all_contacts()
        if option == 6:
            conn.commit()
            conn.close()
            quit()