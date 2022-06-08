class WindowDlg:
    def __init__(self, title: str = None, width: int = 0, height: int = 0) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, new_width: int) -> None:
        if self.verify(new_width):
            if self.__width != new_width:
                self.__width = new_width
                self.show()

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, new_height: int) -> None:
        if self.verify(new_height):
            if self.__height != new_height:
                self.__height = new_height
                self.show()

    def verify(self, value) -> bool:
        return type(value) is int and 0 <= value <= 10_000

    def show(self) -> None:
        print(f"{self.__title}: {self.__width}, {self.__height}")
