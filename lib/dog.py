#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self._name = ""
        self._breed = ""
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

if __name__ == "__main__":
    dog = Dog()
    dog.name = "Buddy"
    dog.breed = "Corgi"
    print(f"Dog's name: {dog.name}")
    print(f"Dog's breed: {dog.breed}")
