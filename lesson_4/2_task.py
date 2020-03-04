# Дан массив целых чисел.
# Нужно найти сумму элементов с индексами у которых сумма бит двоичного представления четна,
# затем перемножить эту сумму и предпоследний элемент исходного массива.
import re

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_digits(number):
    digits = [int(d) for d in str(number)]
    return sum(digits)


def work(li):
    base_list = []
    for j in li:
        bin_j = bin(j)
        res = re.sub('b', '0', bin_j)
        if sum_digits(res) % 2 == 0:
            base_list.append(j)
    result = sum(base_list) * li[-2]
    return result


print(work(first_list))
