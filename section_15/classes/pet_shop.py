class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)
    
    def increase_total_cash(self, cash):
        self.total_cash += cash

    def add_pet(self, pet):
        self.pets.append(pet)
    
    def remove_pet(self, pet):
        pet_index = self.pets.index(pet)

        self.pets.pop(pet_index)
    
    def find_pet_by_name(self, pet_name):
        return self.pets[pet_name]