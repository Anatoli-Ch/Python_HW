# Есть список.
# Нужно реализовать операцию левый и правый сдвиг на указанный шаг.
# Нужно решение с deque и без него.
# Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4].

from collections import deque

while True:
    number = int(input('Введите значение: '))
    lst = input('Заполните список: ').split(' ')

    for _ in range(number):
        elem = lst.pop(0)
        lst.append(elem)
    print('to left', lst)

    for _ in range(number):
        elem = lst.pop()
        lst.insert(0, elem)
    print('to right', lst)

    num = 4
    lst2 = ['1', '2', '3', '4', '5']

    in_deque = deque(lst2)
    in_deque.rotate(num)
    print(in_deque)

    in_deque.rotate(-num)
    print(in_deque)
