# Ваша задача сформировать новый список с именем lst_out, в котором строки с целыми числами будут
# представлены как целые числа (тип int), строки с вещественными числами, как вещественные (тип float),
# а остальные данные - без изменений.


def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


if __name__ == '__main__':
    lst_in = "1 -5.6 True abc 0 23.56 hello".split()
    lst_out = []

    for elem in lst_in:
        lst_out.append(get_number(elem))

    print(lst_out)
