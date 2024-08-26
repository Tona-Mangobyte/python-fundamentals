# Recursion function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120


def dive():
    print('Dive')
    dive()

#dive() # RecursionError: maximum recursion depth exceeded in comparison

def flatten(lol):
    flat = []
    for item in lol:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

print(flatten([1, [2, 3], [4, [5, 6]]])) # [1, 2, 3, 4, 5, 6]
print(flatten([1, [2, [3, 4], [5, 6]]])) # [1, 2, 3, 4, 5, 6]
print(flatten([1, [2, [3, 4], [5, 6, [7, 8]]]])) # [1, 2, 3, 4, 5, 6, 7, 8]

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(0)) # 0
print(fib(1)) # 1

def flatten2(lol):
    flat = []
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
    return flat

print(list(flatten2([1, [2, 3], [4, [5, 6]]]))) # [1, 2, 3, 4, 5, 6]

