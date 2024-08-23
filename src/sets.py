
# Sets are unordered collections of unique elements

# Create a set
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

even_numbers = {0, 2, 4, 6, 8, 8}
print(even_numbers)

# Create a set from a list
odd_numbers = set([1, 3, 5, 7, 9])
print(odd_numbers)

# Create a set from a string
unique_characters = set("Mississippi")
print(unique_characters)

# Create a set from a tuple
unique_characters = set(("M", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"))
print(unique_characters)

# Create a set from a dictionary
unique_characters = set({"M": 1, "i": 4, "s": 4, "p": 2})
print(unique_characters)

# Create a set from a range
whole_numbers = set(range(10))
print(whole_numbers)

# Add an Item with add()
whole_numbers.add(10)
print(whole_numbers)

# Add multiple items with update()
whole_numbers.update([11, 12, 13])
print(whole_numbers)

# Remove an item with remove()
whole_numbers.remove(13)
print(whole_numbers)

# Remove an item with discard()
whole_numbers.discard(12)
print(whole_numbers)

# Remove an item with pop()
whole_numbers.pop()
print(whole_numbers)

# Remove all items with clear()
whole_numbers.clear()
print(whole_numbers)

# Check if an item is in the set
whole_numbers = set(range(10))
print(5 in whole_numbers)
print(15 in whole_numbers)

# Check if an item is not in the set
print(5 not in whole_numbers)
print(15 not in whole_numbers)

# Check if a set is a subset of another set
whole_numbers = set(range(10))
even_numbers = set([0, 2, 4, 6, 8])
print(even_numbers.issubset(whole_numbers))

# Check if a set is a superset of another set
print(whole_numbers.issuperset(even_numbers))

# Check if two sets are disjoint
odd_numbers = set([1, 3, 5, 7, 9])
print(odd_numbers.isdisjoint(even_numbers))

# Find the union of two sets
print(odd_numbers.union(even_numbers))

# Find the intersection of two sets
print(odd_numbers.intersection(even_numbers))

# Find the difference between two sets
print(odd_numbers.difference(even_numbers))

# Find the symmetric difference between two sets
print(odd_numbers.symmetric_difference(even_numbers))

# Find the intersection of two sets and update the first set
odd_numbers.intersection_update(even_numbers)
print(odd_numbers)

# Find the difference between two sets and update the first set
odd_numbers.difference_update(even_numbers)
print(odd_numbers)

# Find the symmetric difference between two sets and update the first set
odd_numbers.symmetric_difference_update(even_numbers)
print(odd_numbers)

# Copy a set
even_numbers = odd_numbers.copy()
print(even_numbers)

# Create a frozen set
frozen_numbers = frozenset(range(10))
print(frozen_numbers)

# Check if a set is a subset of a frozen set
print(even_numbers.issubset(frozen_numbers))

# Check if a set is a superset of a frozen set
print(frozen_numbers.issuperset(even_numbers))

# Check if two sets are disjoint
print(odd_numbers.isdisjoint(frozen_numbers))

# Find the union of two sets
print(odd_numbers.union(frozen_numbers))

# Find the intersection of two sets
print(odd_numbers.intersection(frozen_numbers))

# Find the difference between two sets
print(odd_numbers.difference(frozen_numbers))

# Find the symmetric difference between two sets
print(odd_numbers.symmetric_difference(frozen_numbers))

# Find the intersection of two sets and update the first set
odd_numbers.intersection_update(frozen_numbers)
print(odd_numbers)

# Find the difference between two sets and update the first set
odd_numbers.difference_update(frozen_numbers)
print(odd_numbers)

