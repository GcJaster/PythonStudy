class ObjList:
    def __init__(self, data) -> None:
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        if isinstance(data, str):
            self.__data = data

    @property
    def prev(self) -> object:
        return self.__prev

    @prev.setter
    def prev(self, prev: object) -> None:
        if isinstance(prev, (type(self), type(None))):
            self.__prev = prev

    @property
    def next(self) -> object:
        return self.__next

    @next.setter
    def next(self, next: object) -> None:
        if isinstance(next, (type(self), type(None))):
            self.__next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        if isinstance(obj, ObjList):
            if self.tail:
                self.tail.next = obj
                obj.prev = self.tail
                self.tail = obj
            else:
                self.head = obj
                self.tail = obj

    @staticmethod
    def __check_indx(indx: int) -> bool:
        return isinstance(indx, int) and indx >= 0

    def __get_node(self, indx: int) -> ObjList:
        if self.head and self.__check_indx(indx=indx):
            pos = 0
            node = self.head

            while pos != indx and node:
                node = node.next
                pos += 1

            return node

    def remove_obj(self, indx: int) -> None:
        node = self.__get_node(indx=indx)
        if node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        if node is self.head:
            self.head = node.next if node else None
        if node is self.tail:
            self.tail = node.prev if node else None

    def __len__(self) -> int:
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def __call__(self, indx) -> str:
        node = self.__get_node(indx=indx)
        if node:
            return node.data


if __name__ == '__main__':
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.add_obj(ObjList("Python ООП"))
    linked_lst.remove_obj(3)
    print(linked_lst(1))
