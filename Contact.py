# Contact Book App
contacts={}

while True:
    print("\n Contact Book App:")

    print("1. Create Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Count Contacts")
    print("7. Exit")

    choise =input ("Enter your choise: ")

    if choise == "1":
        name= input ("Enter your name: ")
        if name in contacts:
            print("Contact name {name} already exists.")
        else:
            age = input("Enter your age: ")
            email= input ("Enter your Email: ")
            phone = input("Enter your phone number: ")
            contacts[name] = {
                "age": int(age),
                "email": email,
                "phone": phone
            }
            print(f"Contact name {name} has been created and added successfully.")


    elif choise == "2":
        print ("ALL Contacts ")
        for name, contact in contacts.items():
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Phone: {contact['phone']}")


    elif choise == "3":
        name =input ("Enter contact name to search: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Phone: {contact['phone']}")
        else :
            print("Contact not found.")


    elif choise == "4":
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enter updated email: ")
            phone = input("Enter updated phone number: ")
            contacts[name] = {
                "age": int(age),
                "email": email,
                "phone": phone
            }
            print(f"Contact name {name} has been updated successfully.")
        else:
            print("Contact not found.")


    elif choise == "5":
        name =input("Enter contact name to delete: ")    
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully.")
        else:
            print("Contact not found.")

    elif choise == "6":
        print(f"Total contacts: {len(contacts)}")


    elif choise == "7":
        print("Exiting the Contact Book App.")
        break


    else:
        print("Invalid input. Please try again.")