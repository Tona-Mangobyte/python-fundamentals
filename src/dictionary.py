# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.

# Create and print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

# Change Values
# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
print(thisdict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)


# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)

# Convert with dict()
# It is also possible to use the dict() constructor to make a new dictionary:
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

# Get All Keys with keys()
# The keys() method will return a list of all the keys in the dictionary.
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
x = thisdict.keys()
print(x)

print(list(thisdict.keys()))
print(list(thisdict.values()))
print(list(thisdict.items()))
print(len(thisdict))

# Copy with copy()
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)


# Compare Dictionaries
# When comparing two dictionaries, they will be considered equal if they have the same key:value pairs.
# They will not be considered equal if they have the same key:value pairs but in a different order.
# Compare two dictionaries:
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if dict1 == dict2:
    print("They are the same!")
else:
    print("They are not the same!")

a = {1: [1, 2], 2: [1], 3:[1]}
b = {3: [1], 1: [1, 2], 2: [1]}
print(a == b)  # True
