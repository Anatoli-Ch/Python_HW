# Реализовать RLE сжатие для списка
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
# [(2, 2), (3, 4), (2, 6), (1, 7), (4, 9), (2, 5), (1, 1)]

lst = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]


def rle_func(src):
    result = []
    if src:
        current = src.pop(0)
        counter = 1
        for i in src:
            if i == current:
                counter += 1
            else:
                result.append((counter, current))
                current = i
                counter = 1
        result.append((counter, current))
    return result


print(rle_func(lst))
