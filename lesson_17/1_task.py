# Реализовать класс итератор и генератор типа range. (с 1, 2 и 3 аргументами)
class IterRange1:
    def __init__(self, first, last, step=1):
        self.first = first
        self.last = last
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.first > self.last:
            if self.first == 0:
                raise StopIteration
            self.first -= self.step
            return (self.first + self.step) - self.step

        elif self.first < self.last:
            if self.first == 0:
                raise StopIteration
            self.first += self.step
            if self.first > self.last:
                raise StopIteration
            return (self.first + self.step) - self.step

        elif self.first == self.last:
            raise StopIteration


for i in IterRange1(1, 10):
    print(i)
print()
for i in IterRange1(10, 1):
    print(i)
print()
for i in IterRange1(1, 10, 2):
    print(i)
print()
for i in IterRange1(10, 1, 2):
    print(i)
