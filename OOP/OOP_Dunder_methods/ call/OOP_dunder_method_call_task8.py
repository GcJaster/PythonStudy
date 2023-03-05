from typing import List


class InputDigits:
    Num: List[int] = List[int]

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs) -> Num:
        return [int(i) for i in self.func().split()]


@InputDigits
def input_dg() -> str:
    string = input()
    return string


if __name__ == '__main__':
    res = input_dg()
    print(res)
