import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self): # NEW
      self.customer = Customer("Luke", 150.00, 18, 0)
    
    def test_customer_has_name(self):
       self.assertEqual("Luke", self.customer.name)
    
    def test_customer_has_wallet(self):
       self.assertEqual(150.00, self.customer.wallet)
    
    def test_customer_can_buy_drink(self):
       drink = Drink("Old Fashioned", 5.00, 2)
       pub = Pub("El Rodeo", 100.00)

       self.customer.buy_drink(drink)
       pub.sell_drink(drink)

       self.assertEqual(145.00,self.customer.wallet)
       self.assertEqual(105.00, pub.till)
    
    def test_customer_can_get_drunk(self):
        drink = Drink("Old Fashioned", 5.00, 2)
        self.customer.finish_drink(drink)
        self.assertEqual(2, self.customer.drunkenness)
    
    def test_customer_sobers_up_when_eating(self):
       customer = Customer("Luke", 150.00, 18, 8)
       food = Food("Burger", 10.00, 5)
       customer.eat_food(food)
       self.assertEqual(3, customer.drunkenness)