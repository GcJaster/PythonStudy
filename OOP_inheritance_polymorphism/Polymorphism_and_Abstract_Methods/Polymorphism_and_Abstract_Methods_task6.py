from abc import ABC, abstractmethod
from typing import Union


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """абстрактное свойство (property), название страны (строка)"""

    @property
    @abstractmethod
    def population(self) -> Union[int, float]:
        """абстрактное свойство (property), численность населения (целое положительное число)"""

    @property
    @abstractmethod
    def square(self) -> int:
        """абстрактное свойство (property), площадь страны (положительное число)"""

    @abstractmethod
    def get_info(self) -> str:
        """абстрактный метод для получения сводной информации о стране"""


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: Union[int, float]) -> None:
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def population(self) -> Union[int, float]:
        return self._population

    @population.setter
    def population(self, value: int) -> None:
        self._population = value

    @property
    def square(self) -> int:
        return self._square

    @square.setter
    def square(self, value: Union[int, float]) -> None:
        self._square = value

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


if __name__ == '__main__':
    country = Country("Россия", 140000000, 324005489.55)
    name = country.name
    pop = country.population
    country.population = 150000000
    country.square = 354005483.0
    print(country.get_info())  # Россия: 354005483.0, 150000000
