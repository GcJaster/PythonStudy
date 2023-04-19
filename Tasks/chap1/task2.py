# Модель (Model)
class CalculatorModel:
    def __init__(self):
        self.current_value = 0

    def add(self, value):
        self.current_value += value

    def subtract(self, value):
        self.current_value -= value

    def multiply(self, value):
        self.current_value *= value

    def divide(self, value):
        if value == 0:
            raise ValueError("Ошибка: Деление на ноль невозможно")
        self.current_value /= value

    def clear(self):
        self.current_value = 0


# Представление (View)
class CalculatorView:
    def get_input(self):
        return input("Введите число: ")

    def get_operator(self):
        return input("Выберите операцию (+, -, *, /, c): ")

    def display(self, value):
        print(f"Текущее значение: {value}")

    def error(self, message):
        print(message)


# Контроллер (Controller)
class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def run(self):
        while True:
            self.view.display(self.model.current_value)
            try:
                user_input = self.view.get_input()
                if user_input:
                    value = float(user_input)
                    operator = self.view.get_operator()
                    if operator == "+":
                        self.model.add(value)
                    elif operator == "-":
                        self.model.subtract(value)
                    elif operator == "*":
                        self.model.multiply(value)
                    elif operator == "/":
                        self.model.divide(value)
                    elif operator == "c":
                        self.model.clear()
                    else:
                        raise ValueError("Ошибка: Недопустимый оператор")
                else:
                    break
            except ValueError as e:
                self.view.error(str(e))


if __name__ == "__main__":
    controller = CalculatorController()
    controller.run()