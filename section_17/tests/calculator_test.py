import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase): # NEW
    def test_add(self):
        expected = 5
        actual = add(2, 3)
        self.assertEqual(expected, actual)
    
    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))

    def test_multiply(self):
        self.assertEqual(10, multiply(5, 2))

