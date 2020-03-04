# Есть список объектов.
# Нужно посчитать сколько раз какой тип данных встречается в списке.
lst = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1, 2], {1: 1}]


def counter_func(lt):
    int_list = []
    str_list = []
    float_list = []
    complex_list = []
    lists_list = []
    dict_list = []
    for i in lt:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == str:
            str_list.append(i)
        elif type(i) == float:
            float_list.append(i)
        elif type(i) == complex:
            complex_list.append(i)
        elif type(i) == list:
            lists_list.append(i)
        elif type(i) == dict:
            dict_list.append(i)

    return 'int - {}\nstr - {}\nfloat - {}\ncomplex - {}\nlist - {}\ndict - {}'.format(
        len(int_list), len(str_list), len(float_list), len(complex_list), len(lists_list), len(dict_list))


print(counter_func(lst))
