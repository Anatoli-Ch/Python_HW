# Реализовать класс Point:
#     атрибуты: x, y
#     методы: расстояние между двумя точками, площадь под отрезком
#
# Реализовать класс Polygon:
#     атрибуты: список вершин в порядке обхода по часовой стрелке
#     методы: вычислить периметр, вычислить площадь


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return ((self.x[0] - self.x[1]) ** 2) + ((self.y[0] - self.y[1]) ** 2)

    def area(self):
        pass


class Polygon:
    def __init__(self, *args):
        self.args = args

    def perimeter(self):
        for i in self.args:
            return sum(i)

    def area(self):
        return round(((self.perimeter() / 2) / 2) * ((self.perimeter() / 2) / 2))


obj = Point([-7, -2], [10, 6])
print('Distance between X and Y - {}'.format(Point.distance(obj)))
print('Area under the segment - {}\n'.format(Point.area(obj)))

figure = Polygon([15, 10, 60, 5, 40, 35])
print('Polygon perimeter - {}'.format(Polygon.perimeter(figure)))
print('Polygon area - {}'.format(Polygon.area(figure)))
