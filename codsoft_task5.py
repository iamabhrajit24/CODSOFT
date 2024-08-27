# TASK: Contact book

# This is the contact list, where all contacts will be stored.
contacts = []

# Function to add a new contact
def add_contact():
    while True:
        name = input("Enter Name: ")
        
        # Check for duplicate names
        if any(contact['name'] == name for contact in contacts):
            print("Error: A contact with this name already exists. Please enter a different name.")
            continue
        
        phone = input("Enter Phone Number: ")
        
        # Check if phone number is exactly 10 digits
        if len(phone) != 10 or not phone.isdigit():
            print("Error: Phone number must be exactly 10 digits.")
            continue
        
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        
        # Check if address exceeds 40 words
        if len(address.split()) > 40:
            print("Error: Address cannot be more than 40 words.")
            continue
        
        # Create a dictionary to store the contact details
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        
        # Add the contact to the contacts list
        contacts.append(contact)
        print("Contact added successfully!\n")
        break

# Function to view all contacts
def view_contacts():
    if contacts:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.\n")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter Name or Phone Number to search: ")
    
    # Search through contacts
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.\n")

# Function to update a contact's details
def update_contact():
    search_term = input("Enter the Name or Phone Number of the contact to update: ")
    
    # Find the contact to update
    for contact in contacts:
        if search_term == contact['name'] or search_term == contact['phone']:
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"Enter Name ({contact['name']}): ")
            
            # Prevent updating to an existing contact name
            if new_name and any(c['name'] == new_name for c in contacts):
                print("Error: A contact with this name already exists. Please enter a different name.")
                return
            
            contact['name'] = new_name or contact['name']
            
            new_phone = input(f"Enter Phone Number ({contact['phone']}): ")
            if new_phone:
                if len(new_phone) != 10 or not new_phone.isdigit():
                    print("Error: Phone number must be exactly 10 digits.")
                    return
                contact['phone'] = new_phone
            
            contact['email'] = input(f"Enter Email ({contact['email']}): ") or contact['email']
            
            new_address = input(f"Enter Address ({contact['address']}): ")
            if new_address:
                if len(new_address.split()) > 40:
                    print("Error: Address cannot be more than 40 words.")
                    return
                contact['address'] = new_address
                
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter the Name or Phone Number of the contact to delete: ")
    
    # Find and remove the contact
    for contact in contacts:
        if search_term == contact['name'] or search_term == contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")

# User Interface to interact with the program
def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# To execute the program
if __name__ == "__main__":
    main()
