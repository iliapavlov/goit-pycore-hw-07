import utils.decorators as decorators
from models.address_book import AddressBook
from models.address_book import Record

@decorators.input_error_add
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = f"Contact {name} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added."
    record.add_phone(phone)
    return message

@decorators.input_error_change
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        if record.edit_phone(old_phone, new_phone):
            message = f"Contact {name} updated."
        else:
            message = f"Contact {name} does not have number {old_phone}."
    else:
        message = f"Contact '{name}' not found."
    return message

@decorators.input_error_search
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        message = str(record)
    else:
        message = f"Contact '{name}' not found."
    return message

@decorators.input_error_search
def delete_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        book.delete(name)
        message = f"Contact '{name}' has been deleted"
    else:
        message = f"Contact '{name}' not found."
    return message

@decorators.input_error_search
def show_all(book: AddressBook):
    if not book.data:
        message = "Contacts list is empty"
    else:
        message = "\n".join([str(record) for record in book.data.values()])
    return message

@decorators.input_error_add
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = f"Contact {name} updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact {name} added."
    record.add_birthday(birthday)
    return message

@decorators.input_error_search
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        message = record.show_birthday()
    else:
        message = f"Contact '{name}' not found."
    return message

@decorators.input_error_search
def birthdays(book: AddressBook):
    message = "There is no celebrates next week"
    if not book.data:
        message = "Contacts list is empty"
    else:
        birthday_list = book.get_upcoming_birthdays()
        lines = []
        for contact in birthday_list:
            line = ' celebrates '.join(contact.values())
            lines.append(line)
        message = '\n'.join(lines)
    return message
