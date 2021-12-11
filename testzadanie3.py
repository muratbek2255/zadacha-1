import unittest
from zadanie3 import MyMath

class TestCubes(unittest.TestCase):
    def test_init(self):

        x=MyMath(5,2)
        self.assertEqual(x.a, 5)
        self.assertEqual(x.b, 2)
    def test_operation_sub(self):
        x = MyMath(5,2)
        self.assertEqual(x.substraction(),3)
    def test_operation_add(self):
        x = MyMath(5, 2)
        self.assertEqual(x.addition(), 7)
    def test_operation_div(self):
        x = MyMath(5, 2)
        self.assertEqual(x.division(), 2.5)
    def test_operation_mul(self):
        x = MyMath(5, 2)
        self.assertEqual(x.multiplication(), 10)