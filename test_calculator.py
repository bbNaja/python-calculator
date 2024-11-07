import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add1(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(9, 2), 7)

    def test_multipy2(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_multipy(self):
        self.assertEqual(self.calc.multiply(4, 4), 16)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 0), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(20, 3), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()