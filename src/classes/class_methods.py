# Class Methods
# Class methods are methods that are bound to the class itself and not to any object.

# They have the access to the state of the class as it takes
# a class parameter that points to the class and not the object instance.

# It can modify a class state that would apply across all the instances of the class.

class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print(f'{name} walks with {cls.legs} legs')

Animal.walk('Dog')
