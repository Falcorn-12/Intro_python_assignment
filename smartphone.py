# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        return f"Calling {number} from {self.model}..."

    def take_photo(self):
        return f"{self.model} takes a photo 📸"

# Inheritance Example (Polymorphism/Encapsulation)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game):
        return f"Playing {game} smoothly on {self.model} with {self.cooling_system} cooling!"

# Testing
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB")
phone2 = GamingPhone("Asus", "ROG Phone 7", "512GB", "Liquid Cooling")

print(phone1.call("0712345678"))
print(phone2.take_photo())
print(phone2.play_game("PUBG Mobile"))
