from __future__ import annotations
from typing import Union, List
from dataclasses import dataclass, field


@dataclass
class Box:
    """Storage box for various things."""

    box: List[Thing] = field(default_factory=list)

    def add_thing(self, obj: Thing):
        """Append object into box."""
        if not isinstance(obj, Thing):
            raise TypeError("Объект должен иметь тип Thing.")
        self.box.append(obj)

    def get_things(self) -> List[Thing]:
        """Return list of the Thing objects."""
        return self.box

    def __eq__(self, other: Box) -> bool:
        """Comparison of each item from two boxes."""
        self.__verify_data(other)
        sbl, obl = self.get_things(), other.get_things()
        return len(sbl) == len(obl) and all([t in obl for t in sbl])

    @staticmethod
    def __verify_data(other) -> None:
        """Verify of type Object."""
        if not isinstance(other, Box):
            raise TypeError("The operand on the right must be of type Box.")


@dataclass
class Thing:
    """Any thing."""

    name: str = ''
    mass: Union[int, float] = 0

    def __eq__(self, other: Thing) -> bool:
        """Check the case-insensitive name and the mass of two things."""
        self.__verify_data(other)
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    @staticmethod
    def __verify_data(other) -> None:
        """Verify of type Object."""
        if not isinstance(other, Thing):
            raise TypeError("The operand on the right must be of type Thing.")


def main() -> None:
    b1 = Box()
    b2 = Box()

    b1.add_thing(Thing('мел', 100))
    b1.add_thing(Thing('тряпка', 22))
    b1.add_thing(Thing('доска', 2000))

    b2.add_thing(Thing('тряпка', 22))
    b2.add_thing(Thing('мел', 100))
    b2.add_thing(Thing('доска', 2000))

    print(b1 == b2)


if __name__ == '__main__':
    main()
