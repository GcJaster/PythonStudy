class Student:
    """Class describing the student"""

    def __init__(self, fio: str, group: str):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # lecture grade
        self._house_marks = []  # homework grade

    def add_lect_marks(self, mark: int) -> None:
        self._lect_marks.append(mark)

    def add_house_marks(self, mark: int) -> None:
        self._house_marks.append(mark)

    def __str__(self) -> str:
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    """Class describing a mentor"""

    _name_job = None

    def __init__(self, fio: str, subject: str) -> None:
        self._fio = fio
        self._subject = subject

    def __str__(self,) -> str:
        if hasattr(self, '_name_job'):
            if self._name_job is not None:
                return f'{self._name_job} {self._fio}: предмет {self._subject}'
        return str(-1)

    def set_mark(self, student, mark) -> NotImplementedError:
        raise NotImplementedError(f"В доочернем классе {self.__class__} не переопределён метод set_marks")


class Lector(Mentor):
    """Class describing the lecturer """

    _name_job = 'Лектор'

    def __init__(self, fio: str, subject: str) -> None:
        super().__init__(fio, subject)

    def set_mark(self, student: Student, mark: int) -> None:
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    """Class describing the expert"""

    _name_job = 'Эксперт'

    def __init__(self, fio: str, subject: str) -> None:
        super().__init__(fio, subject)

    def set_mark(self, student: Student, mark: int) -> None:
        student.add_house_marks(mark)


if __name__ == '__main__':
    lector = Lector("Балакирев С.М.", "Информатика")
    reviewer = Reviewer("Гейтс Б.", "Информатика")
    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]
    lector.set_mark(students[0], 4)
    lector.set_mark(students[1], 2)
    reviewer.set_mark(students[0], 5)
    reviewer.set_mark(students[1], 3)
    for p in persons + students:
        print(p)