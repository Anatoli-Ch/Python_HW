# Реализовать класс итератора, который будет возвращать переданную ему коллекцию в обратном порядке.
class IterCollection:
    def __init__(self, collection):
        self.collection = collection

    def __getitem__(self, index):
        return self.collection[index][::-1]


collect = IterCollection([1, 2, 3, 4, 5, 'A', 'B', 'C', 'D'])
print(collect[:])
