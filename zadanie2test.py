import unittest
from zadanie2 import TriangleChecker

class TestTriangleChecker(unittest.TestCase):
    def test_init(self):

        x = TriangleChecker(2,2,3)
        self.assertEqual(x.a, 2)
        self.assertEqual(x.b, 2)
        self.assertEqual(x.c, 3)

    def test_str(self):
        s = ('dy', 2, 3)
        self.assertIsInstance(s, str)

    def test_negative(self):
        s2 = (-2, 2, 3)
        self.assertEqual(s2, 'Нельзя вводить негаивные числа!')

    def test_ravny(self):
        s3 = (10, 2, 3)
        self.assertEqual(s3, 'Треугольник не получился!!')



