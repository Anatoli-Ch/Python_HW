# Дана строка “spam and eggs or eggs with spam”. Посчитать сколько раз встретился каждый символ.
starting_string = 'spam and eggs or eggs with spam'
another_string = ''.join(starting_string.split())
second_string = set(another_string)
print(starting_string)
for j in second_string:
    print('{} встречается'.format(j), starting_string.count(j), 'раз.')


# starting_string = 'spam and eggs or eggs with spam'
# another_string = ''.join(starting_string.split())
# lst = []
# for i in another_string:
#    lst.append(i)
# lst = set(lst)
# print(starting_string)
# for j in lst:
#    print('{} встречается'.format(j), starting_string.count(j), 'раз.')
