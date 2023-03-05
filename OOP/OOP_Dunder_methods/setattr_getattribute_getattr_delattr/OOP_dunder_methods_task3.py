from typing import List


class LessonItem:
    """ Lesson in module"""

    title: str
    practices: int
    duration: int

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.duration = duration
        self.practices = practices

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__[key]):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.__annotations__.items():
            return False
        del item


class Module:
    """ Module of lessons in course"""

    name: str
    lessons: List[LessonItem]

    def __init__(self, name: str):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    """ Educational course containing modules of lessons """

    name: str
    modules: List[Module]

    def __init__(self, name: str) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


def maim():
    course = Course("Python ООП")
    module_1 = Module("Часть первая")
    module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
    module_1.add_lesson(LessonItem("Урок 3", 5, 800))
    course.add_module(module_1)
    module_2 = Module("Часть вторая")
    module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
    course.add_module(module_2)


if __name__ == '__main__':
    maim()