# Реализовать класс со своей операцией сложения.
# Например класс точка с 3-мя координатами. Сложение - сложение соответствующих координат.


class Coordinates:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return Coordinates(self.a + other.a, self.b + other.b, self.c + other.c)

    def __str__(self):
        return '{} ({})'.format(self.__class__.__name__, self.__dict__)


p1 = Coordinates(1, 0, 0)
p2 = Coordinates(0, 1, 0)
p3 = Coordinates(0, 0, 1)
p4 = Coordinates(1, 1, 1)
print(p1 + p2 + p3 + p4)
