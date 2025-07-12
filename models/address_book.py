from collections import UserDict
from datetime import datetime
from datetime import timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")

class Birthday(Field):
    def __init__(self, value: str):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(parsed_date)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone_to_delete):
        self.phones = [phone for phone in self.phones if phone.value != phone_to_delete]


    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index] = Phone(new_phone)
                return True
        return False

    def find_phone(self, searched_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == searched_phone:
                return self.phones[index]

    def add_birthday(self, date):
        self.birthday = Birthday(date)
    
    def show_birthday(self):
        if self.birthday:
            return f"Birthday of {self.name.value}: {self.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"No birthday set for {self.name.value}."

    def __str__(self):
        return f"Info about contact. name: {self.name.value}; phones: {', '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
    # def delete(self, name: str) -> bool:
    # return self.data.pop(name, None) is not None


    def get_upcoming_birthdays(self):
        days_period = 7 
        today = datetime.today().date()
        today_year = datetime.today().year
        celebrants = []
        for name in self.data:
            birthday_month = self.data.get(name).birthday.value.month
            birthday_day = self.data.get(name).birthday.value.day
            birthday_this_year = datetime(year=today_year, month=birthday_month, day=birthday_day).date()

            if birthday_this_year < today:
                pass # відмічатиме в наступному році
            else:
                dates_diff = (birthday_this_year - today).days
                if dates_diff < days_period:
                    day_of_week = birthday_this_year.weekday()
                    if day_of_week == 5: 
                        congratulation_date = birthday_this_year + timedelta(days=2)
                    elif day_of_week == 6:
                        congratulation_date = birthday_this_year + timedelta(days=1)
                    else:
                        congratulation_date = birthday_this_year
                    birthday_boy = {
                        "name": name, 
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                    }
                    celebrants.append(birthday_boy)
        return celebrants


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # john_record.add_birthday("17.07.2025")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("17.07.2025")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # # Знаходження та редагування телефону для John
    john = book.find("John")
    if john.edit_phone("1234567890", "1112223333"):
        print("номер замінено")
    else:
        print("номер не знайдено")

    print(john)
    john.remove_phone("1112223333")
    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    print(book.get_upcoming_birthdays())

    # Видалення запису Jane
    book.delete("Jane")

if __name__ == "__main__":
    main()
