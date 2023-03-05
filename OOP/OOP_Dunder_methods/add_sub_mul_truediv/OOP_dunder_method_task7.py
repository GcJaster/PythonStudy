from typing import NoReturn, Tuple, List


class MaxPooling:
    step: Tuple[int, int]
    size: Tuple[int, int]

    def __init__(self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)) -> NoReturn:
        self.step = step
        self.size = size

    def __call__(self, matrix) -> List[List[int]]:
        rectangle = len(matrix[0])
        for elem in matrix:
            if len(elem) != rectangle:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for number in elem:
                if not isinstance(number, (int, float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")

        lst_out = []
        for i in range(0, (len(matrix) // self.step[0]) * self.step[0], self.step[0]):
            lst_tmp = []
            for j in range(0, (len(matrix[0]) // self.step[1]) * self.step[1], self.step[1]):
                max_temp = matrix[i][j]

                for i_internal in range(i, i + self.size[0]):
                    for j_internal in range(j, j + self.size[1]):
                        if max_temp < matrix[i_internal][j_internal]:
                            max_temp = matrix[i_internal][j_internal]

                lst_tmp.append(max_temp)
            lst_out.append(lst_tmp)
        return lst_out


def main() -> NoReturn:
    mp = MaxPooling(step=(2, 2), size=(2, 2))
    res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    for row in res:
        print(*row)


if __name__ == '__main__':
    main()