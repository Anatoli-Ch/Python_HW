# реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
# (простое число - делится только на себя и 1)
# вход:
# 456
# 0
# вывод:
# 2^3 * 3 * 19

number = int(input('Введите число: '))
num = 2
while num < number:
    if number % num == 0:
        print(num)
        number //= num
    else:
        num += 1
print(number)
