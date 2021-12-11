import unittest
from class_soda import Soda

class TestSoda(unittest.TestCase):

   def test_init(self):
       s = Soda('Cola')
       self.assertEqual(s.dabavka, 'Cola')


if __name__ == "__main__":
unittest.main()