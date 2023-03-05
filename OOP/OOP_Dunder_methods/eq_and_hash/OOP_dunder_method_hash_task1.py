from __future__ import annotations
from typing import Union
from dataclasses import dataclass


@dataclass
class Rect:
    """Creating a rectangular object in the upper left corner at x and n coordinates."""
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]

    def __eq__(self, other: Rect) -> bool:
        """Comparing the Height and Width of Two Objects."""
        return self.height == other.height and self.width == other.width

    def __hash__(self):
        """Getting a hash of an object's width and height."""
        return hash((self.width, self.height))


def main() -> None:
    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)

    h1, h2 = hash(r1), hash(r2)  # h1 == h2 # True
    print(h1 == h2)


if __name__ == '__main__':
    main()
