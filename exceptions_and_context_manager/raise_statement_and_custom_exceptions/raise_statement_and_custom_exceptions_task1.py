# Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception. После этого объявите
# еще два класса-исключения, унаследованные от базового класса StringException:
# NegativeLengthString - ошибка, если длина отрицательная;
# ExceedLengthString - ошибка, если длина превышает заданное значение;
# Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки
# исключения ExceedLengthString.


class StringException(Exception):
    """Класс исключение для строк"""


class NegativeLengthString(StringException):
    """Класс исключение для строки, если длина отрицательная"""


class ExceedLengthString(StringException):
    """Класс исключение для строки, если длина превышает заданное значение"""


if __name__ == '__main__':
    try:
        raise ExceedLengthString
    except NegativeLengthString:
        print("NegativeLengthString")
    except ExceedLengthString:
        print("ExceedLengthString")
    except StringException:
        print("StringException")