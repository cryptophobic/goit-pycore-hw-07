import sys

from AddressBook import AddressBook
from Record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as err:
            return str(err)

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact_details(args: list, book: AddressBook) -> str:
    name, phone_number = args
    record = book.find(name)
    if record is not None:
        record.add_phone_number(phone_number)
    else:
        record = Record(name)
        record.add_phone_number(phone_number)
        book.add_record(record)

    return "Contact added."


@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def phone_contact(args: list, book: AddressBook) -> str:
    [name] = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")

    return '; '.join(p.value for p in record.phones)


def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()
    close = False
    while not close:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact_details(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(phone_contact(args, book))
            case "birthday":
                print(add_birthday(args, book))
            case "greetings":
                print(book.get_upcoming_birthdays())
            case "all":
                print(book)
            case _ if command in ["close", "exit"]:
                close = True
            case _:
                sys.stderr.write("Invalid command.\n"
                                 "Available commands are: close, exit, hello, add, change, phone, all\n")

    print("Good bye!")


if __name__ == "__main__":
    main()
