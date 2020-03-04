# * Дан отсортированный список. Реализуйте бинарный поиск.
from random import randint


def binary_search(array, key_value, left=0, right=None):
    if left < 0:
        raise ValueError('Must be positive value!')
    if right is None:
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle + 1)


lst = []
for i in range(15):
    lst.append(randint(1, 50))
lst.sort()
print(lst)

key = int(input('Введите значение: '))
flag, idx = binary_search(lst, key)


print('Index =', idx)

if not flag:
    lst.insert(idx, key)

print(lst)
