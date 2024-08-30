from collections import namedtuple

# Create a namedtuple class
Point = namedtuple('Point', ['x', 'y'])
point = Point(20, 30)
print(point.x, point.y)  # 20 30

# Access the fields by index
print(point[0], point[1])  # 20 30

# Convert the namedtuple to a dictionary
print(point._asdict())  # {'x': 20, 'y': 30}

# Replace the fields
point = point._replace(x=100)
print(point.x, point.y)  # 100 30

