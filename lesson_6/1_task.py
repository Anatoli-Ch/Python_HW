# Найти самую длинную последовательность из одинаковых чисел в списке, вывести длину и само число.
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]
# '9' - 4

numbers_lst = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]


def summary(ls):
    result_list = []
    clone_ls = ls.copy()
    count = 0
    for i in ls:
        for j in clone_ls:
            if i == j:
                count += 1
        result_list.append(count)
        count = 0
    output1 = str(max(ls))
    output2 = max(result_list)
    return "'{}' - {}".format(output1, output2)


print(summary(numbers_lst))
