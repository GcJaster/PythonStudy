from typing import NoReturn, Any


class StackObj:
    def __init__(self, data) -> NoReturn:
        self.__data = data
        self.__next = None

    @property
    def next(self) -> Any:
        return self.__next

    @next.setter
    def next(self, obj) -> NoReturn:
        self.__next = obj


class Stack:
    def __init__(self) -> NoReturn:
        self.top = None

    def push_back(self, obj) -> NoReturn:
        """Push StackObj to the end of a linked list"""
        new_node = obj

        if self.top is None:
            self.top = obj
            return

        cur = self.top
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def pop_back(self):
        """Delete last element from linked list"""
        if self.top is None:
            print("None")
            return

        if self.top.next is None:
            self.top = None
            return

        cur = self.top
        while cur.next:
            if cur.next.next is None:
                cur.next = None
                break
            else:
                cur = cur.next

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self

    def __imul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


def main():
    a = StackObj(1)
    b = StackObj(2)
    c = StackObj(3)
    s = Stack()
    s.push_back(a)
    s.push_back(b)
    s.push_back(c)
    s = s + StackObj(4)
    s.pop_back()
    s.pop_back()
    s.pop_back()
    s = s * ['data_1', 'data_2']
    print(s.__dict__)


if __name__ == '__main__':
    main()