import os
import re

def clear ():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_id(): #Function to return new ID for a contact
    last_id = max(contact_list.keys()) if contact_list else 0
    return last_id + 1


def is_valid_email(email):
    # Regex pattern for validating an email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def is_valid_phone_number(phone_number):
    # Regex pattern for validating a phone number (e.g., 10 digits)
    pattern = r'\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}'
    return re.match(pattern, phone_number) is not None


contact_list = {}

def new_contact():
    new_contact_id = new_id()
    
    while True:
        contact = input ("Please enter a new contact: \n")
        phone_number = None
        email = None

        while True:
            if phone_number is None:
                phone_number = input ("Please enter a phone number: \n")
                if not is_valid_phone_number(phone_number):
                    print("Invalid phone number. Please enter a 10-digit phone number.")
                    phone_number = None
                continue
            email = input ("Please enter an email: \n")
            if not is_valid_email(email):
                print("Invalid email address. Please enter a valid email.")
                continue
            clear()
            print (f"Contact: {contact}; Phone number: {phone_number}; Email: {email}")
            correct = input ("Does this information look correct? (y/n) \n")
            if correct.lower() == 'y':
                #Create new contact
                contact_list[new_contact_id] = {'Contact': contact, 'Phone Number': phone_number, 'Email': email}
                print("Contact saved successfully!")
                input("Press Enter to return to the main menu...")
                clear()
                return
            else:
                clear ()
                print("Let's try again.\n")
                break


def edit_contact():
    if not contact_list:
        print("No contacts available to edit.")
        input("Press Enter to return to the main menu...")
        return
    
    print("Contact List:\n")
    for contact_id, contact_info in contact_list.items():
        print(f'Contact ID: {contact_id}')
        print(f'Contact: {contact_info["Contact"]}')
        print(f'Phone Number: {contact_info["Phone Number"]}')
        print(f'Email: {contact_info["Email"]}')
        print("-" * 20)

    while True:
        try:
            contact_id = int(input("Enter the contact ID you'd like to edit:\n"))
            if contact_id in contact_list:
                while True:
                    contact = input("Please enter a new contact name:\n")
                    phone_number = None
                    email = None
                    while True:
                        phone_number = input("Please enter a new phone number:\n")
                        if not is_valid_phone_number(phone_number):
                            print("Invalid phone number. Please enter a 10-digit phone number.")
                            phone_number = None
                            continue
                        email = input("Please enter a new email:\n")
                        if not is_valid_email(email):
                            print("Invalid email address. Please enter a valid email.")
                            continue
                        clear()
                        print(f"Contact: {contact}; Phone number: {phone_number}; Email: {email}")
                        correct = input("Does this information look correct? (y/n)\n")
                        if correct.lower() == 'y':
                            contact_list[contact_id] = {'Contact': contact, 'Phone Number': phone_number, 'Email': email}
                            print("Contact edited successfully!")
                            input("Press Enter to return to the main menu...")
                            clear()
                            return
                        else:
                            clear()
                            print("Let's try again.\n")
                            break
            else:
                print(f"Contact ID {contact_id} is not in the list. Please enter a valid contact ID.")
        except ValueError:
            print("Invalid input. Please enter a numeric contact ID.")



def delete_contact ():
    if not contact_list:
        print("No contacts available to delete.")
        input("Press Enter to return to the main menu...")
        return

    print ("Which contact would you like to remove from the list? \n")
    print("Contact List: \n")
    for contact_id, contact_info in contact_list.items():
            print (f'Contact ID: {contact_id}')
            print (f'Contact: {contact_info['Contact']}')
            print (f'Phone Number: {contact_info['Phone Number']}')
            print (f'Email: {contact_info['Email']}')
            print("-" * 20)

    while True:
        try:
            contact_id = int(input ("Enter the contact ID you'd like to remove from the list. \n"))
            if contact_id in contact_list:
                removed_contact = contact_list.pop(contact_id)
                print (f"{removed_contact['Contact']} has been removed from the list.")
                input("Press Enter to return to the main menu...")
                clear()
                break
            else:
                print(f"Contact ID {contact_id} is not in the list. Please enter a valid contact ID.")
        except ValueError:
            print("Invalid input. Please enter a numeric contact ID.")

def search_contacts():
    if not contact_list:
        print("No contacts available to search.")
        input("Press Enter to return to the main menu...")
        return

    while True:
        ans = input ("Enter the ID, name, email or phone number of the contact you'd like to search for: \n")
        
        found_contact = False
        for contact_id, contact_info in contact_list.items():
            if ans == str(contact_id) or ans == contact_info['Contact'] or ans == contact_info['Phone Number'] or ans == contact_info["Email"]:
                clear()
                print ("Found 1 existing contact: \n")
                print (f'Contact ID: {contact_id}')
                print (f'Contact: {contact_info['Contact']}')
                print (f'Phone Number: {contact_info['Phone Number']}')
                print (f'Email: {contact_info['Email']}')
                found_contact = True
                break
        if found_contact:
             input("Press Enter to return to the main menu...")
             clear()
             return
        else:
                print ("Contact not found. Please try again")

def display_contacts():
    if not contact_list:
        print("No contacts available to view.")
        input("Press Enter to return to the main menu...")
        clear()
        return
    
    else:
        print("Contact List: \n")
        for contact_id, contact_info in contact_list.items():
            print (f'Contact ID: {contact_id}')
            print (f'Contact: {contact_info['Contact']}')
            print (f'Phone Number: {contact_info['Phone Number']}')
            print (f'Email: {contact_info['Email']}')
            print("-" * 20)

    input ("Press Enter to return to the main menu...")
    clear()

def export_contact(contact_list):
    try:
        with open('contact_list.txt', 'w') as file:
            for contact_id, contact_info in contact_list.items():
                file.write(f"{contact_id},{contact_info['Contact']},{contact_info['Phone Number']},{contact_info['Email']}\n")
        print("Contact list successfully exported!")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")
    input("Press Enter to return to the main menu...")
    clear()


def import_contact():
    try:
        with open('contact_list.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 4:
                    print(f"Skipping malformed line: {line}")
                    continue
                contact_id, contact_name, phone_number, email = parts
                if not is_valid_phone_number(phone_number):
                    print(f"Skipping invalid phone number: {phone_number}")
                    continue
                if not is_valid_email(email):
                    print(f"Skipping invalid email: {email}")
                    continue

                contact_list[int(contact_id)] = {'Contact': contact_name, 'Phone Number': phone_number, 'Email': email}
            print("Contacts imported successfully!")   
    except FileNotFoundError:
        print("The file 'contact_list.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to return to the main menu...")
    clear()               

def main ():
    while True:
        ans = input ('''
        Welcome to the Contact Management System!

        Menu:
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
        7. Import contacts from a text file
        8. Quit

        Please enter your selection (1-8): ''')
        if ans == '1':
            clear()
            new_contact() # Function to add a new contact
        elif ans == '2':
            clear()
            edit_contact() # Function to edit a contact
        elif ans == '3':
            clear()
            delete_contact() # Function to delete a contact
        elif ans == '4':
            clear()
            search_contacts() # Function to search for a contact
        elif ans == '5':
            clear()
            display_contacts() # Function to display all contacts
        elif ans == '6':
            clear()
            export_contact(contact_list) # Function to export contacts to a text file
        elif ans == '7':
            clear()
            import_contact() # Function to import contacts from a text file
        elif ans == '8':
            print("Thanks for using our contact management system!")
            break
        else:
            print('Please enter a valid number.')

main()
