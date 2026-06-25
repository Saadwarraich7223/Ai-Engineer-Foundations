# Day 07 � Mini Project 1 � Contact Book CLI
# Date: June 30, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

import json


contacts={}

def load_contacts():
    global contacts

    with open("contacts.json", "r") as file:
            contacts = json.load(file)
            
load_contacts()
def show_menu():
    print("1. Add a contact")
    print("2. List all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")


def add_contact():
    name=input("ENTER NAME: ")
    email=input("ENTER EMAIL: ")
    num=input("ENTER NUMBER: ")
    contacts[name]={
        "email":email,
        "num":num
    }
    print(f'Contact for {name} added successfully')
    
def get_all_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n{:<20} {:<30} {:<15}".format("NAME", "EMAIL", "PHONE"))
    print("-" * 70)

    for name, info in contacts.items():
        print(
            "{:<20} {:<30} {:<15}".format(
                name,
                info["email"],
                info["num"]
            )
        )
        
        
def search_contact():
    search=input("Search: ").lower()
    found = False
    for name,info in contacts.items():
        if (search in name.lower() 
            or search in info['email'].lower()
            or search in info["num"]):
            print("\n FOUND:")
            print(f'Name: {name}')
            print(f'Email: {info['email']}')
            print(f'Number: {info['num']}')
            found=True
        if not found:
            print("Contact Not found")
        
            
def update_contact():
    name = input("Enter contact name to update: ")

    if name not in contacts:
        print("Contact not found.")
        return

    new_email = input("New email: ")
    new_phone = input("New phone: ")

    contacts[name]["email"] = new_email
    contacts[name]["phone"] = new_phone

    print("Contact updated successfully.")
    
def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
        
def export_json():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    print("Contacts exported to contacts.json")


while True:
    show_menu()
    choice=input("Choose an option: ")
    
    if choice == "1":
        add_contact()

    elif choice == "2":
        get_all_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        export_json()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
    