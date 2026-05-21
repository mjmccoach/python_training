import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self): # NEW
      self.drink = Drink("Old Fashioned", 5.00, 2)
    
    def test_drink_has_a_name(self):
       self.assertEqual("Old Fashioned", self.drink.name)
    
    def test_drink_has_a_price(self):
       self.assertEqual(5.00, self.drink.price)
