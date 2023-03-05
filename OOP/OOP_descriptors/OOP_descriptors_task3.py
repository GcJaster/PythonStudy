class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=3, max_length=100):
        self._min_length = min_length
        self._max_length = max_length

    def __verify_str_val(self, value):
        if type(value) == str and self._min_length <= len(value) <= self._max_length:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__verify_str_val(value):
            setattr(instance, self.name, value)


class PriceValue:
    _MIN_VALUE = 0

    def __init__(self, max_value=10000):
        self._max_value = max_value

    def __verify_val(self, value):
        if type(value) in (int, float) and self._MIN_VALUE < value < self._max_value:
            return True
        return False

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.__verify_val(value):
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price
