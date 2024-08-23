# Tuples are immutable sequences of arbitrary objects. Tuples are like lists, but they are immutable and are usually used to store collections of heterogeneous data.

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

a, b, c = marx_tuple
print(a, b, c)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

combining_tuples = ('Groucho', 'Chico', 'Harpo') + ('Zeppo', 'Gummo')
print(combining_tuples)

duplicate_tuple = ('Groucho',) * 3
print(duplicate_tuple)

# Compare Tuples
a_tuple = (7, 2)
b_tuple = (7, 2, 9)
print(a_tuple == b_tuple)
print(a_tuple < b_tuple)


# Iterate with for and in
words = ('fresh','out', 'of', 'ideas')
for word in words:
    print(word)


