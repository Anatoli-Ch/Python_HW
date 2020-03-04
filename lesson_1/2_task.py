# даны два словаря
# a = {'a': 1, 'b': 4, 't': 67}
# b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
# 2.1 найти ключи которые есть в обоих словарях
# 2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
# 2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались
from collections import Counter

a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
print('Ключи которые есть в обоих словарях:')
for keys in b:
    if keys in a:
        print(keys)
print('Ключи из второго словаря, которых нет в первом:')
for key in b:
    if key not in a:
        print(key)

c = Counter()
for element in a, b:
    c.update(element)

d = {}
d.update(c)
print(d)

