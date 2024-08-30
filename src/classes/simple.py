# Class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return self.name + ' says Meow!'

    def __str__(self):
        return f'{self.name} is {self.age} years old'

cat = Cat('Felix', 5)
print(cat.speak())
print(cat)

class Yugo(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return self.name + ' says Meow! Meow!'

    def __str__(self):
        return super().__str__()


cat2 = Yugo('Tom', 10)
print(cat2.speak())
print(cat2)

print(isinstance(cat, Cat))
print(isinstance(cat2, Yugo))
print(issubclass(Yugo, Cat))
