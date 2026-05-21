import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self): # NEW
      self.pub = Pub("El Rodeo", 100.00)
    
    def test_pub_has_name(self): # NEW
        self.assertEqual("El Rodeo", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_pub_serves_customer_if_overage(self):
        customer = Customer("Luke", 150.00, 18, 0)
        self.assertTrue(self.pub.can_serve(customer))
    
    def test_pub_does_not_serve_customer_if_underage(self):
        customer = Customer("Morgan", 150.00, 17, 0)
        self.assertFalse(self.pub.can_serve(customer))
    
    def test_pub_serves_customer_if_sober_enough(self):
        customer = Customer("Morgan", 150.00, 18, 0)
        self.assertTrue(self.pub.can_serve(customer))
    
    def test_pub_doesnt_serve_customer_if_too_drunk(self):
        customer = Customer("Morgan", 150.00, 18, 7)
        self.assertFalse(self.pub.can_serve(customer))
 

