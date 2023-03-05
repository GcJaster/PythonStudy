class StackObj:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.__last = None

    def push_back(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            self.__last.next = obj
        self.__last = obj

    def push_front(self, obj: StackObj) -> None:
        if self.top is None:
            self.__last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def get_obj(self, index: int) -> StackObj:
        if type(index) != int or not (0 <= index < len(self)):
            raise IndexError("неверный индекс")

        for i, obj in enumerate(self):
            if i == index:
                return obj

    def __iter__(self) -> StackObj:
        h = self.top
        while h:
            yield h
            h = h.next
        return self

    def __getitem__(self, item: int) -> str:
        return self.get_obj(item).data

    def __setitem__(self, key: int, value: str) -> None:
        self.get_obj(key).data = value

    def __len__(self) -> int:
        return sum(1 for _ in self)


def main() -> None:
    st = Stack()
    st.push_back(StackObj('g1'))
    st.push_back(StackObj('g2'))
    st.push_back(StackObj('g3'))
    st.push_back(StackObj('g4'))
    st.push_front(StackObj('g0'))

    st[1] = 'g11'  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
    data = st[1]  # получение данных из объекта стека по индексу
    n = len(st)  # получение общего числа объектов стека
    print(data)
    print(n)

    for obj in st:  # перебор объектов стека (с начала и до конца)
        print(obj.data)  # отображение данных в консоль


if __name__ == '__main__':
    main()
