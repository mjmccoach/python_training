class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
    
    def sell_drink(self, drink):
        self.till += drink.price

    def can_serve(self, customer):
        if customer.age >= 18 and customer.drunkenness <= 6:
            return True
        return False