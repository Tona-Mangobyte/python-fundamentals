# List

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Accessing elements in a list
print(weekdays[0]) # Monday

for day in weekdays:
    print(day)

# Get Items with a Slice
print(weekdays[0:3]) # ['Monday', 'Tuesday', 'Wednesday']
print(weekdays[:3]) # ['Monday', 'Tuesday', 'Wednesday']
print(weekdays[3:]) # ['Thursday', 'Friday']
print(weekdays[-1]) # Friday
print(weekdays[-2:]) # ['Thursday', 'Friday']

# Changing, Adding, and Removing Elements
print(weekdays.reverse()) # None
print(weekdays) # ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
weekdays.remove('Monday')
print(weekdays) # ['Friday', 'Thursday', 'Wednesday', 'Tuesday']
weekdays.append('Monday')
print(weekdays) # ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
weekdays.insert(0, 'Sunday')
print(weekdays) # ['Sunday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
del weekdays[0]

# Combine Lists by Using extend() or +
weekend = ['Saturday', 'Sunday']
# weekdays += weekend
weekdays.extend(weekend)
print(weekdays) # ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Saturday', 'Sunday']

# Find an Element in a List
print(weekdays.index('Wednesday')) #

# Check if an Element Is in a List
print('Wednesday' in weekdays) # True

# Get the Length of a List
print(len(weekdays)) # 7

# Using the range() Function
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

# List Comprehensions
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# Reorder Items with sort() or sorted()
weekdays.sort()
print(weekdays) # ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']

numbers = [2, 1, 4.0, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [1, 2, 3, 4.0]

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4.0]
numbers.sort(reverse=True)
print(numbers) # [4.0, 3, 2, 1]


# Copy a List
weekdays_copy = weekdays[:]
print(weekdays_copy) # ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
weekdays_copy2 = weekdays.copy()
print(weekdays_copy2) # ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']

# List of Lists
lists = [weekdays, weekend]
print(lists) # [['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'], ['Saturday', 'Sunday']]
print(lists[0]) # ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
print(lists[1]) # ['Saturday', 'Sunday']

# List of Tuples
tuples = [(1, 2), (3, 4)]
print(tuples) # [(1, 2), (3, 4)]
print(tuples[0]) # (1, 2)
print(tuples[1]) # (3, 4)

# List of Dictionaries
dictionaries = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 24}]
print(dictionaries) # [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 24}]
print(dictionaries[0]) # {'name': 'John', 'age': 25}
print(dictionaries[1]) # {'name': 'Jane', 'age': 24}

# List of Sets
sets = [{1, 2}, {3, 4}]
print(sets) # [{1, 2}, {3, 4}]
print(sets[0]) # {1, 2}
print(sets[1]) # {3, 4}

# List of Strings
strings = ['hello', 'world']
print(strings) # ['hello', 'world']
print(strings[0]) # hello
print(strings[1]) # world

# List of Numbers
numbers = [1, 2, 3, 4]
print(numbers) # [1, 2, 3, 4]
print(numbers[0]) # 1
print(numbers[1]) # 2

# List of Booleans
booleans = [True, False]
print(booleans) # [True, False]
print(booleans[0]) # True
print(booleans[1]) # False

# List of None
none = [None, None]
print(none) # [None, None]
print(none[0]) # None
print(none[1]) # None

# List of Mixed Types
mixed = ['hello', 1, True]
print(mixed) # ['hello', 1, True]
print(mixed[0]) # hello
print(mixed[1]) # 1
print(mixed[2]) # True

# List of Lists
lists = [[1, 2], [3, 4]]
print(lists) # [[1, 2], [3, 4]]
print(lists[0]) # [1, 2]
print(lists[1]) # [3, 4]

# Compare Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2]
print(list1 == list2) # True
print(list1 == list3) # False

