from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter) # Counter({'spam': 3, 'eggs': 1})

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter) # Counter({'eggs': 2, 'bacon': 1})

print(breakfast_counter + lunch_counter) # Counter({'spam': 3, 'eggs': 3, 'bacon': 1})
print(breakfast_counter - lunch_counter) # Counter({'spam': 3})
print(breakfast_counter & lunch_counter) # Counter({'eggs': 1})
print(breakfast_counter | lunch_counter) # Counter({'spam': 3, 'eggs': 2, 'bacon': 1})

