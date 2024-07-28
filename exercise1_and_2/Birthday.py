from datetime import datetime
from Field import Field


class Birthday(Field):

    def __init__(self, birthday):
        try:
            print(birthday)
            birthday_parsed = datetime.strptime(birthday, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(birthday_parsed)
