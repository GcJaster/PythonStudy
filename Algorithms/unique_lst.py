# список уникальных чисел больше 5 с сохранением порядка
def get_unique(array: list[int]) -> list[int]:
    """Получаем список уникальных чисел с сохранением порядка"""

    dublicate = {}
    unique_lst = []
    for num in array:
        dublicate[num] = dublicate.get(num, 0) + 1
        if num > 5 and dublicate.get(num) < 2:
            unique_lst.append(num)

    return unique_lst


def main():
    lst = [100, 1, 10110, 100]
    print(get_unique(lst))


if __name__ == '__main__':
    main()