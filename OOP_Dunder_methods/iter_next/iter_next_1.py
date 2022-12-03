from typing import Union


class Person:
    def __init__(
            self,
            fio: str,
            job: str,
            old: int,
            salary: Union[int, float],
            year_job: int) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._length_attrs = len(self._attrs)
        self._iter_index = 0

    def check_index(self, index: int) -> None:
        if type(index) != int or not (-self._length_attrs <= index < self._length_attrs):
            raise IndexError("неверный индекс")

    def check_data_type(self, old_data, new_data) -> None:
        if type(new_data) != type(old_data):
            raise TypeError("несовместимые типы данных")

    def __getitem__(self, item):
        self.check_index(item)
        return getattr(self, self._attrs[item])

    def __setitem__(self, key, value):
        self.check_index(key)
        self.check_data_type(self._attrs[key], value)
        setattr(self, self._attrs[key], value)

    def __iter__(self) -> iter:
        self._iter_index -= 1
        return self

    def __next__(self):
        if self._iter_index < self._length_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        raise StopIteration


def main() -> None:
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[0] = 'Балакирев С.М.'
    for v in pers:
        print(v)
    # pers[5] = 123  # IndexError


if __name__ == '__main__':
    main()
