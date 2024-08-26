# Decorators for functions

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5)) # 8
cooler_add_ints = document_it(add_ints) # Running function: add_ints ...
print(cooler_add_ints(3, 5)) # 8

@document_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 15)) # 18


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5)) # 64
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64
# 64
