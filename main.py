filename = "contacts.txt"
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                name, email, phone = line.strip().split(',')
                contacts[name] = {'email': email, 'phone': phone}
            return contacts
    except FileNotFoundError:
        return {}

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['email']},{info['phone']}\n")


def add_contact(contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    contacts[name] = {'email': email, 'phone': phone}
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        email = input("Enter new email (leave blank to keep current): ")
        phone = input("Enter new phone number (leave blank to keep current): ")
        if email:
            contacts[name]['email'] = email
        if phone:
            contacts[name]['phone'] = phone
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    file_path = "contacts.txt"
    contacts = load_contacts(file_path)

    while True:
        print("\nMenu:")
        print("1. Add new contact")
        print("2. View contacts")
        print("3. Edit existing contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(file_path, contacts)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
