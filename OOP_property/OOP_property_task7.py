class PhoneNumber:
    number = 0
    fio = ""

    def __init__(self, number: int, fio: str) -> None:
        if self.verify(number):
            self.number = number
        self.fio = fio

    def __repr__(self) -> str:
        return f"{self.fio}: {self.number}"

    @staticmethod
    def verify(number):
        if not type(number) is int and len(str(number)) != 11:
            raise ValueError("Number must be int and length is 11")


class PhoneBook:
    __records = []
    __instance = None

    def __new__(cls, *args, **kwargs) -> object:
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def add_phone(self, phone: PhoneNumber) -> None:
        'добавление нового номера телефона (в список);'
        self.__records.append(phone)

    def remove_phone(self, indx: int) -> None:
        'удаление номера телефона по индексу списка;'
        self.__records.pop(indx)

    def get_phone_list(self) -> list:
        'получение списка из объектов всех телефонных номеров'
        return self.__records

    def __repr__(self) -> str:
        return f"{self.get_phone_list()}"
