class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self.msg = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            key, value = tuple(kwargs.items())[0]
            self.msg = f'Значение первичного ключа {key} = {value} недопустимо'


    def __str__(self):
        return self.msg



if __name__ == '__main__':
    try:
        raise PrimaryKeyError(id = -10.5)
    except PrimaryKeyError as e:
        print(e)

