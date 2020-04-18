# Выберите класс из пердыдущих дз и покройте его тестами. Не сильно сложное, но чтоб был какой-то функционал.
# Можно использовать любой фреймворк для тестов или даже несколько.
# Предпочтительно pytest.

import unittest
from numbers import Numbers


class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.A = Numbers(5, 6)
        self.B = Numbers(6, 10)
        self.C = Numbers(5.0, 6.0)
        self.D = Numbers(-5, -6)

    def test_init(self):
        self.assertEqual((self.A.x, self.A.y), (float(5), float(6)))
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)))
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)))
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)))

    def test_str(self):
        self.assertTrue(str(self.A) == "(5.0, 6.0)")
        self.assertTrue(str(self.B) == "(6.0, 10.0)")
        self.assertTrue(str(self.C) == "(5.0, 6.0)")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)")


if __name__ == '__main__':
    unittest.main()
