from typing import Deque, List
import abc


class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def positive(self):
        pass

    @abc.abstractmethod
    def negative(self):
        pass


class Calculator:
    def on(self):
        print("Калькулятор запущен")

    def off(self):
        print("Калькулятор выключен")

    def plus(self):
        print(f"складываю числа")

    def minus(self):
        print(f"вычитаю числа")


class CalculatorWorkCommand(ICommand):
    def __init__(self, calculator: Calculator):
        self.calculator: Calculator = calculator

    def positive(self):
        self.calculator.on()

    def negative(self):
        self.calculator.off()


class CalculatorAdJustCommand(ICommand):
    def __init__(self, calculator: Calculator):
        self.calculator: Calculator = calculator

    def positive(self):
        self.calculator.plus()

    def negative(self):
        self.calculator.minus()


class KeyBoard:
    def __init__(self):
        self.__commands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__commands[button] = command

    def press_on(self, button):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    calculator = Calculator()

    keyboard = KeyBoard()
    keyboard.set_command(0, CalculatorWorkCommand(calculator))
    keyboard.set_command(1, CalculatorAdJustCommand(calculator))

    keyboard.press_on(0)
    keyboard.press_on(1)

    keyboard.press_cancel()
    keyboard.press_cancel()