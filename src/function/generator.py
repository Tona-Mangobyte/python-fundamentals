# Generator Functions
print(sum(range(1, 101))) # 5050

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range) # <function my_range at 0x7f9b3c1b7d30>
ranger = my_range(1, 5)
print(ranger) # <generator object my_range at 0x7f9b3c1b7f68>
for x in ranger:
    print(x) # 1 2 3 4

