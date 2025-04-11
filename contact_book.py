#!/usr/bin/env python3

import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="project1user",
        password="P@ssword123",
        database="Contact_Book"
)
except Exception as e:
    print(f"{e} Error connecting Mysql to Python")

cursor = db.cursor()






class Contact:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.phone = int(input("Enter the phone number: "))
        self.email= input("Enter the email: ")
        insert_data_query = "INSERT INTO contact_details (name, phone_number, email) VALUES (%s, %s, %s)"
        self.values = (self.name, self.phone, self.email)
        cursor.execute(insert_data_query, self.values)
        db.commit()

def view_all_contacts(cursor):
    view_all_query = "SELECT name, phone_number, email FROM contact_details"
    cursor.execute(view_all_query)
    return cursor.fetchall()

def view_contact(cursor, name):
    view_contact_query = "SELECT name, phone_number, email FROM contact_details WHERE name=%s"
    value = (name,)
    cursor.execute(view_contact_query, value)
    return cursor.fetchone()

def delete_contact(cursor, name):
    delete_contact_query = "DELETE FROM contact_details WHERE name=%s"
    value = (name,)
    cursor.execute(delete_contact_query, value)

    
while True:
    a = int(input("Welcome to the Contact Book. Select and option\n1.) Add a contact\n2.) View all contacts\n3.) Search a contact by name\n4.) Delete a contact\n"))
    if a == 1:
        contact1 = Contact()
    elif a == 2:
        all_contacts = view_all_contacts(cursor)
        for contact in all_contacts:
            print(contact)
    elif a == 3:
        contact_name = input("Whose contact would you like? ")
        searched_contact = view_contact(cursor, contact_name)
        for contact in searched_contact:
            print(contact)
    elif a == 4:
        deleted_contact = input("Which contact would you like to delete?")
        delete_contact(cursor, deleted_contact)
