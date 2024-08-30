# Multiple Inheritance
# A class can be derived from more than one base classes in Python, similar to C++.

class Animal:
    def speak(self):
        print("Animal Speaking")

class Horse(Animal):
    def __init__(self):
        print("Horse is ready")

    def speak(self):
        print("Neigh")

class Donkey(Animal):
    def __init__(self):
        print("Donkey is ready")

    def speak(self):
        print("Hee-Haw")

class Mule(Donkey, Horse):
    def __init__(self):
        Donkey.__init__(self)
        Horse.__init__(self)
        print("Mule is ready")

    def speak(self):
        Donkey.speak(self)
        Horse.speak(self)
        print("Hee-Haw Neigh")

class Hinny(Horse, Donkey):
    def __init__(self):
        Horse.__init__(self)
        Donkey.__init__(self)
        print("Hinny is ready")

    def speak(self):
        Horse.speak(self)
        Donkey.speak(self)
        print("Neigh Hee-Haw")


mule = Mule()
hinny = Hinny()
mule.speak()
hinny.speak()
