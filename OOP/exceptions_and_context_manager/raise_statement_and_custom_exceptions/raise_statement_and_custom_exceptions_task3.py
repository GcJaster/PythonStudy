from datetime import datetime


class DateError(Exception):
    """Класс исключение для даты"""


class DateString:
    def __init__(self, date_string) -> None:
        self.date = datetime.strptime(date_string, '%d.%m.%Y').strftime('%d.%m.%Y')

    def __str__(self):
        return f'{self.date}'


if __name__ == '__main__':
    date_string = '1.222.1812'
    try:
        date = DateString(date_string)
        print(date)
    except ValueError:
        print("Неверный формат даты")


