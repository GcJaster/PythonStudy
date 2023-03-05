def selection_sort(alist: list[int]) -> list[int]:
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

lst = [1,2,-30, 0]
print(f'Sorted list: {selection_sort(lst)}')
