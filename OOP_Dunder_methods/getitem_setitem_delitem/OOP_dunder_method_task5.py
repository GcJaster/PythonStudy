from typing import Union, Any


class StackObj:
    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj

class Stack:
    def __init__(self):
        self.top = None
        self.__count_objs = 0

    def push(self, obj):
        last = self[self.__count_objs - 1] if self.__count_objs > 0 else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

    def pop(self):
        if self.__count_objs == 0:
            return None

        last = self[self.__count_objs - 1]

        if self.__count_objs == 1:
            self.top = None
        else:
            self[self.__count_objs - 2].next = None

        self.__count_objs -= 1
        return last

    def __getitem__(self, item: int) -> StackObj:
        self.check_index(item)

        node = self.top
        count = 0

        while node and count < item:
            node = node.next
            count += 1

        return node

    def __setitem__(self, key: int, value: StackObj) -> None:
        self.check_index(key)

        node = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = node.next
        if prev:
            prev.next = value

    def check_index(self, indx: int) -> None:
        if type(indx) != int or not(0 <= indx < self.__count_objs):
            raise IndexError("неверный индекс")


def main():
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st[1] = StackObj("new obj2")
    print(st[2].data)  # obj3
    print(st[1].data)  # new obj2
    # res = st[3]  # исключение IndexError


if __name__ == '__main__':
    main()