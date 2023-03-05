from dataclasses import dataclass


@dataclass
class BookStudy:
    name: str
    author: str
    year: int

    def __hash__(self) -> int:
        """Returns the hash of a post by title and author."""
        return hash((self.name.lower(), self.author.lower()))


def main() -> None:
    lst_bs = []

    lst_in = ["Python; Балакирев С.М.; 2020",
              "Python ООП; Балакирев С.М.; 2021",
              "Python ООП; Балакирев С.М.; 2022",
              "Python; Балакирев С.М.; 2021"
              ]

    for string in lst_in:
        name, author, year = string.split('; ')
        lst_bs.append(BookStudy(name, author, year))

    unique_books = len(set(map(lambda x: hash(x), lst_bs)))
    print(unique_books)     # 2


if __name__ == '__main__':
    main()