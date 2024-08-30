from dataclasses import dataclass

@dataclass
class DataClass:
    name: str
    value: int

    def __str__(self):
        return f'{self.name}={self.value}'

    def __repr__(self):
        return f'{self.name}={self.value}'

    def __add__(self, other):
        return DataClass(self.name, self.value + other.value)

    def __sub__(self, other):
        return DataClass(self.name, self.value - other.value)

    def __mul__(self, other):
        return DataClass(self.name, self.value * other.value)

    def __truediv__(self, other):
        return DataClass(self.name, self.value / other.value)

    def __floordiv__(self, other):
        return DataClass(self.name, self.value // other.value)

    def __mod__(self, other):
        return DataClass(self.name, self.value % other.value)

    def __pow__(self, other):
        return DataClass(self.name, self.value ** other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __and__(self, other):
        return DataClass(self.name, self.value & other.value)

    def __or__(self, other):
        return DataClass(self.name, self.value | other.value)

    def __xor__(self, other):
        return DataClass(self.name, self.value ^ other.value)

    def __lshift__(self, other):
        return DataClass(self.name, self.value << other.value)

    def __rshift__(self, other):
        return DataClass(self.name, self.value >> other.value)

    def __neg__(self):
        return DataClass(self.name, -self.value)

    def __pos__(self):
        return DataClass(self.name, +self.value)

    def __abs__(self):
        return DataClass(self.name, abs(self.value))

    def __invert__(self):
        return DataClass(self.name, ~self.value)

    def __round__(self,
                    n: int = 0):
            return DataClass(self.name, round(self.value, n))



if __name__ == '__main__':
    x = DataClass('x', 10)
    y = DataClass('y', 20)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x // y)
    print(x % y)
    print(x ** y)
    print(x == y)
    print(x != y)
    print(x < y)
    print(x <= y)
    print(x > y)
    print(x >= y)
    print(x & y)
    print(x | y)
    print(x ^ y)
    print(x << y)
    print(x >> y)
    print(-x)
    print(+x)
    print(abs(x))
    print(~x)
    print(round(x, 2))
    print(x)
    print(y)
    print(x == x)
