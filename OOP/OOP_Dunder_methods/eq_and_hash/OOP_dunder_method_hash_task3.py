from __future__ import annotations
from dataclasses import dataclass, field
from itertools import count
from typing import Dict, List, Union


@dataclass
class Record:
    """Record about a person to write to the database."""

    fio: str
    descr: str
    old: int
    pk: int = field(default_factory=lambda: next(counter))

    def __eq__(self, other: Record) -> bool:
        """Comparison of hashes of two entries by name and age."""
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        """Returns the hash of the entry by name and age."""
        return hash((self.fio.lower(), self.old))


@dataclass
class DataBase:
    """Database for storing records of people."""

    path: str
    dict_db: Dict[Record, List[Record]] = field(default_factory=dict)

    def write(self, record) -> None:
        """Write new record into database"""
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)     # if hash of record already on database record

    def read(self, pk) -> Union[List[Record], None]:
        """Returns a record for the specified pk."""
        res = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, res))
        return obj[0] if len(obj) > 0 else None


def main() -> None:

    lst_in = ["Балакирев С.М.; программист; 33",
              "Кузнецов Н.И.; разведчик-нелегал; 35",
              "Суворов А.В.; полководец; 42",
              "Иванов И.И.; фигурант всех подобных списков; 26",
              "Балакирев С.М.; преподаватель; 33"
             ]

    db = DataBase('database.db')
    for string in lst_in:
        db.write(Record(*map(str.strip, string.split(';'))))

    count = 0
    for rec, val in db.dict_db.items():
        count += 1
        print(f"Rec#{count} \t\t\t ", rec, '\n', f"\rvalue of rec #{count} ", val, '\n')


if __name__ == '__main__':
    counter = count()
    main()
