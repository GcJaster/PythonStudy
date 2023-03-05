def get_second_max(array: list[int]):
    """Получаем 1й и 2й максимум"""
    try:
        if array[0] > array[1]:
            max1, max2 = array[0], array[1]
        else:
            max1, max2 = array[1], array[0]
    except IndexError:
        return None

    for num in array[2:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and max1 != num:
            max2 = num

    return max1, max2


def main():
    lst = [100, 1, 10110, 100]
    print(get_second_max(lst))


if __name__ == '__main__':
    main()