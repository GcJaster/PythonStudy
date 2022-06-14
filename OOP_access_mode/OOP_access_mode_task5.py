from typing import Any, List


class ObjList:
    def __init__(self, data) -> None:
        self.__next = None
        self.__prev= None
        self.__data = data

    def set_next(self, obj) -> None:
        self.__next = obj

    def set_prev(self, obj) -> None:
        self.__prev = obj

    def get_next(self) -> object:
        return self.__next

    def get_prev(self) -> object:
        return self.__prev

    def set_data(self, data) -> None:
        self.__data = data

    def get_data(self) -> Any:
        return self.__data


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        if self.head:
            temp = obj
            temp.set_prev(self.tail)
            self.tail.set_next(temp)
            self.tail = temp
        else:
            self.head = obj
            self.tail = obj


    def remove_obj(self) -> None:
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self) -> List[Any]:
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result


def main():
    lst = LinkedList()
    lst.add_obj(ObjList("данные 1"))
    lst.add_obj(ObjList("данные 2"))
    lst.add_obj(ObjList("данные 3"))
    res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
    print(res)


if __name__ == '__main__':
    main()
