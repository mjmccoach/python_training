import unittest

from src.fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_returns_fizz_when_divisible_by_3(self):
        self.assertEqual("Fizz", Fizzbuzz.fizzbuzz(18))
    
    def test_returns_buzz_when_divisible_by_5(self):
        self.assertEqual("Buzz", Fizzbuzz.fizzbuzz(10))

    def test_returns_fizzbuzz_when_divisible_by_3_and_5(self):
        self.assertEqual("Fizzbuzz", Fizzbuzz.fizzbuzz(15))

    def test_returns_value_when_not_divisible_by_3_or_5(self):
        self.assertEqual("7", Fizzbuzz.fizzbuzz(7))