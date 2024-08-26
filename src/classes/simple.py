# Class
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'

cat = Cat('Felix')
print(cat.speak())

