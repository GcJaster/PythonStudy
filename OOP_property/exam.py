class DecisionTree:
    @classmethod
    def predict(cls, root, x: list):
        obj = root

        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next

        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        return obj.right

class TreeObj:
    def __init__(self, indx: int, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


if __name__ == '__main__':
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

    x = [0, 1, 1]
    res = DecisionTree.predict(root, x)  # будет программистом
    print(res)