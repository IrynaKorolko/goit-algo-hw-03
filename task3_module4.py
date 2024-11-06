def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact (args, contacts):
    if len (args) != 2:
        return "Error: Please provide both a username and new phone number."
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."
    
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please provide a username."
    name = args[0]
    
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Error: Contact not found."
    
def show_all (contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():  
        result.append(f"{name}: {phone}")  
    
    return "\n".join(result)  

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print (change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()