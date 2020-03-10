# Реализовать иерархию классов геометрических фигур.
# Базовый класс должен обязывать потомков реализовать методы - периметр и площадь. Потомки:
# 	Треугольник
#         конструктор: принимает список сторон и проверяет, что в списке сторон ровно 3
#         периметр
#         площадь
#
# 	Прямоугольник:
# 	    все аналогично треугольнику, только 2 стороны
# 	Круг:
#         все аналогично треугольнику, только принимает радиус


class Figures:
    def p(self):
        raise Exception('Error data')

    def s(self):
        raise Exception('Error')


class Tirangle(Figures):
    def __init__(self, args):
        if len(args) != 3:
            super().p()
        else:
            perimeter = sum(args)
            area = (perimeter // 2) * (perimeter // 2 - args[0]) * (perimeter // 2 - args[1]) * (
                        perimeter // 2 - args[2])
            print('Tirangle:\n\tPerimeter - {}\n\tarea - {}\n'.format(perimeter, area // (perimeter // 2)))


class Rectangle(Figures):
    def __init__(self, args):
        if len(args) != 2:
            super().s()
        else:
            perimeter = sum(args)
            area = args[0] * args[1]
            print('Rectangle:\n\tPerimeter - {}\n\tarea - {}\n'.format(perimeter, area))


class Circle(Figures):
    def __init__(self, radius):
        if len(radius) != 1:
            super().s()
        else:
            pi = 3.14
            area = pi * (radius[0] * radius[0])
            print('Circle:\n\tarea - {}'.format(area))


T = Tirangle([3, 4, 5])
R = Rectangle([5, 10])
C = Circle([6])
