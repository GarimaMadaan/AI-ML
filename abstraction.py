from abc import ABC, abstractmethod

class Animal(ABC, abstractmethod):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")        

lion = Lion()
lion.make_sound() # Roar!

cow = Cow()
cow.make_sound() # Moo!        