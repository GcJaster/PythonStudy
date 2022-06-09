from typing import List


class Node:
    def __init__(self, data: str) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, new_data) -> None:
        self.__data = new_data

    @property
    def next(self) -> object:
        return self.__next

    @next.setter
    def next(self, new_next) -> None:
        if self.__check_next_item(new_next):
            self.__next = new_next

    @staticmethod
    def __check_next_item(item) -> bool:
        return isinstance(item, Node) or item is None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, node: Node) -> None:
        if not self.top:
            self.top = node
            return

        cur = self.top
        while cur.next:
            cur = cur.next
        cur.next = node

    def pop(self) -> None:
        if self.top.next is None:
            self.top = None
            return

        cur = self.top
        while cur.next:
            if cur.next.next is None:
                cur.next = None
                break
            cur = cur.next

    def get_data(self) -> List[str]:
        res = []
        cur = self.top
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res


st = Stack()
st.push(Node("obj1"))
st.push(Node("obj2"))
st.push(Node("obj3"))
st.pop()
st.pop()
print(st.get_data())