from abc import ABC, abstractmethod


class Desc:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class StackObj:
    data = Desc()
    next = Desc()

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека"""

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека"""


class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self.__last = None

    def push_back(self, obj):
        if self.__last:
            self.__last.next = obj
        self.__last = obj

        if self._top is None:
            self._top = obj

    def pop_back(self):
        temp = self._top

        if temp is None:
            return

        while temp.next and temp.next != self.__last:
            temp = temp.next

        if self._top == self.__last:
            temp2 = self._top
            self._top = self.__last = None
            return temp2
        else:
            temp2 = self.__last
            self.__last = temp
            return temp2


if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj("obj 1"))
    obj = StackObj("obj 2")
    st.push_back(obj)
    del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
    del_obj2 = st.pop_back()
    print(del_obj2.data)