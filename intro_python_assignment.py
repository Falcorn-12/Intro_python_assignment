# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# Inheritance example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game}!")


# Activity 2: Polymorphism Challenge

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")


class Bird(Animal):
    def move(self):
        print("Bird is flying 🕊️")


class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")


# --- Testing ---
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S23", 256)
    phone1.info()
    phone1.call("123456789")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, "Adreno 730")
    gaming_phone.info()
    gaming_phone.play_game("Genshin Impact")

    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()