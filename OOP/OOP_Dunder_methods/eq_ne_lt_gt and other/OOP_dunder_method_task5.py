class FileAcceptor:
    def __init__(self, *args) -> None:
        self.lst_exts = list(args)

    def __call__(self, filename: str) -> bool:
        return filename.split('.')[-1] in self.lst_exts

    def __add__(self, other) -> object.__class__:
        if not isinstance(other, FileAcceptor):
            raise TypeError("Операнд справа должен иметь тип FileAcceptor!")

        return FileAcceptor(*(self.lst_exts + other.lst_exts))


def main() -> None:
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

    acceptor1 = FileAcceptor("jpg", "jpeg", "png")
    acceptor2 = FileAcceptor("png", "bmp")
    acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
    print("acceptor12.lst_exts: ", acceptor12.lst_exts)

    filenames1 = list(filter(acceptor1, filenames))
    filenames2 = list(filter(acceptor2, filenames))
    print("filenames with acceptor1: ", filenames1)
    print("filenames with acceptor2: ", filenames2)

    acceptor_images = FileAcceptor("jpg", "jpeg", "png")
    acceptor_docs = FileAcceptor("txt", "doc", "xls")
    filenames = list(filter(acceptor_images + acceptor_docs, filenames))
    print("filenames with both acceptors: ", filenames)


if __name__ == '__main__':
    main()