# Дан список большой вложенности, нужно его развернуть в 1d
# [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]

lst = [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]

result = []
for sublist in lst:
    for x in sublist:
        result.append(x)
print(result)

# res = [x for sublist in lst for x in sublist]
