# Attribute Access
# Attribute access is the mechanism used to access the attributes of an object.

class Duck:
    def __init__(self, input_color='white'):
        self._color = input_color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color



duck = Duck()
print(duck.get_color())  # Output: white
duck.set_color('blue')
print(duck.get_color())  # Output: blue
duck._color = 'green'
print(duck._color)  # Output: green

class Cat:
    def __init__(self, input_color='white'):
        self.__color = input_color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


cat = Cat()
print(cat.color)  # Output: white
cat.color = 'blue'
print(cat.color)  # Output: blue
cat.__color = 'green'
print(cat.__color)  # Output: green
print(cat.color)  # Output: blue
print(cat._Cat__color)  # Output: blue


# Properties for Computed Values

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return 3.14159 * (self.radius ** 2)

c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 7
print(c.diameter)  # Output: 14
print(c.area)  # Output: 153.93844

