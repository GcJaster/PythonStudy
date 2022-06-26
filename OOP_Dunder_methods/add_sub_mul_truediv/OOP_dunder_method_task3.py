class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        new_node = obj

        if self.top is None:
            self.top = obj
            return

        cur = self.top
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def pop_back(self):
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


# if __name__ == '__main__':
#     main()