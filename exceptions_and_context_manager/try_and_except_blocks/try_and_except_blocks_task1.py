if __name__ == '__main__':
    lst_in = "8 11 abcd -7.5 2.0 -5".split()

    res = 0
    for i in lst_in:
        try:
            res += int(i)
        except ValueError:
            continue

    print(res)