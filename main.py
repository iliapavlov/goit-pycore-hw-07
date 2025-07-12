import handlers.contact_list as contact_list
import utils.io as io
from models.address_book import AddressBook

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = io.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(contact_list.add_contact(args, book))

        elif command == "change":
            print(contact_list.change_contact(args, book))

        elif command == "phone":
            print(contact_list.show_phone(args, book))

        elif command == "all":
            print(contact_list.show_all(book))

        elif command == "add-birthday":
            print(contact_list.add_birthday(args, book))

        elif command == "show-birthday":
            print(contact_list.show_birthday(args, book))

        elif command == "birthdays":
            print(contact_list.birthdays(book))
        
        elif command == "delete":
            print(contact_list.delete_contact(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
