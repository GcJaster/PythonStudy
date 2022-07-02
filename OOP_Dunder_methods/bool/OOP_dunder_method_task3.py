from typing import Union
from dataclasses import dataclass


@dataclass
class Line:
    x1: Union[int, float, complex]
    y1: Union[int, float, complex]
    x2: Union[int, float, complex]
    y2: Union[int, float, complex]

    def __len__(self):
        return int(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)


def main() -> None:
    line = Line(0, 0, 0, 0)
    print(len(line))


if __name__ == '__main__':
    main()