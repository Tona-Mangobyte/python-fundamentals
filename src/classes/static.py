# Static Methods are methods that are bound to the class rather than the object of the class.

# They do not require a class instance creation. So, they are not dependent on the state of the object.

# The difference between a static method and a class method is:

# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

class Animal:
    legs = 4
    @staticmethod
    def walk(name):
        print(f'{name} walks with {Animal.legs} legs')

Animal.walk('Dog')
