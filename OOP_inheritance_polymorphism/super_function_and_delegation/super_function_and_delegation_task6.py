class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False



def main() -> None:
    sl = SoftList("python")
    a = sl[0]  # 'p'
    b = sl[-1]  # 'n'
    c = sl[6]  # False
    d = sl[-7]  # False
    print(a, b, c, d)

if __name__ == '__main__':
    main()
