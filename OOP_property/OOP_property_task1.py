class Car:
    def __init__(self) -> None:
        self.__model = None

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model) -> None:
        if self.check_model(new_model):
            self.__model = new_model

    @staticmethod
    def check_model(model) -> bool:
        return type(model) is str and 2 <= len(model) <= 100


car = Car()
car.model = "Toyota"
print(car.__dict__)
