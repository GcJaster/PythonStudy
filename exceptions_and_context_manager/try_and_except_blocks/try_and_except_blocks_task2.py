# Ваша задача сформировать новый список с именем lst_out, в котором строки с целыми числами будут
# представлены как целые числа (тип int), строки с вещественными числами, как вещественные (тип float),
# а остальные данные - без изменений.


def convert(value):
    for T in (int, float, str):
        try:
            return T(value)
        except:
            pass


if __name__ == '__main__':
    lst_in = "1 -5.6 True abc 0 23.56 hello".split()
    lst_out = []

    for elem in lst_in:
        lst_out.append(convert(elem))

    print(lst_out)
