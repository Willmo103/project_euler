arr = [2, 4, 5, 5, 5, 5, 6, 9, 8]


def first_last(array, char):
    first = -1
    last = -1
    for i in range(0, len(array)):
        if array[i] == char and first == -1:
            first = i
        if array[i] == char:
            last = i
    return [first, last]


print(first_last(arr, 9))
