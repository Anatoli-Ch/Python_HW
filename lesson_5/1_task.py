# Дан двумерный список чисел. Подсчитать сумму нечетных чисел в каждой строке
lst = [
    [1, 2, 3, 4, 5, 6],
    [10, 21, 13, 14, 52, 63, 34],
    [2],
    [3, 2, 6],
    [35, 47],
    [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
    [100, 200, 300, 400, 500, 600]
]

sum_list = []
for lists in lst:
    for elements in lists:
        if elements % 2 != 0:
            sum_list.append(elements)
    thesum = 0
    for elem in sum_list:
        thesum = thesum + elem
    sum_list.clear()
    print(thesum)
