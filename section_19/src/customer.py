class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
    
    def buy_drink(self, drink):
        self.wallet -= drink.price
    
    def finish_drink(self, drink):
        self.drunkenness += drink.alcohol_level
    
    def eat_food(self, food):
        self.drunkenness -= food.rejuvenation_level