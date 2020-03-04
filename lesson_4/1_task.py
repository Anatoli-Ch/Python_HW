# Дан массив.
# Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами.
# Функция должна иметь вид: def swap(target_list, item_index1, item_index2).

lst = ['a', 1, 2, 3, 4, 5, 'b']
print(lst)
first_id = int(input('Введите первый индекс: '))
second_id = int(input('Введите второй индекс: '))


def swap(target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    return target_list


print(swap(lst, first_id, second_id))
