a, b = input().split()
try:
    a, b = map(int, (a, b))
except ValueError:
    try:
        a, b = map(float, (a, b))
    except ValueError:
        pass
finally:
    print(a + b)