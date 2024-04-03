import bot_functions

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = bot_functions.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(bot_functions.add_contact(args, contacts))
        elif command == "change":
            print(bot_functions.change_contact(args, contacts))
        elif command == "phone":
            print(bot_functions.phone_from_contacts(args, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name} has this phone number: {phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
