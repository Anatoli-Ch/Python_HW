# Дана строка S. Нужно распечатать её подстроками длиной w.
# Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

S = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4
for i in range(0, len(S), w):
    end = i + w
    result = S[i:end]
    print(result)
