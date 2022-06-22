class Model:
    def query(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        if len(self.__dict__) != 0:
            return f"Model: " + ", ".join([f"{key} = {item}" for key, item in self.__dict__.items()])

        return f"Model"


if __name__ == '__main__':
    model = Model()
    model.query(id=1, fio='Sergey', old=33)
    print(str(model))