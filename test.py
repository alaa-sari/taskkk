import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_add(self):
        # Test addition functionality (add 20 to the input)
        result = self.calc.add(3)
        self.assertEqual(result, 23)  # 3 + 20 = 23
        
        result = self.calc.add(-1)
        self.assertEqual(result, 19)  # -1 + 20 = 19
        
        result = self.calc.add(0)
        self.assertEqual(result, 20)  # 0 + 20 = 20

    def test_subtract(self):
        # Test subtraction functionality (subtract 20 from the input)
        result = self.calc.subtract(10)
        self.assertEqual(result, -10)  # 10 - 20 = -10
        
        result = self.calc.subtract(-5)
        self.assertEqual(result, -25)  # -5 - 20 = -25

if __name__ == '__main__':
    unittest.main()
