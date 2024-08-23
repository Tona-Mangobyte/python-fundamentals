# Function definition

def sayHello():
    print("Hello World")

sayHello() # Output: Hello World

def agree():
    return True

if agree():
    print("Splendid!")
else:
    print("That was unexpected.")
# Output: Splendid!

# Function with arguments
def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin')) # Output: Rumplestiltskin Rumplestiltskin

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
print(commentary('blue')) # Output: I've never heard of the color blue.

# Function with default arguments
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken')) # Output: {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}
print(menu('dunkelfelder', 'duck', 'doughnut')) # Output: {'wine': 'dunkelfelder', 'entree': 'duck', 'dessert': 'doughnut'}

# Function with variable arguments
def print_args(*args):
    print('Positional argument tuple:', args)
print_args() # Output: Positional argument tuple: ()
print_args(3, 2, 1, 'wait!', 'uh...') # Output: Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')

# Function with variable keyword arguments
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon') # Output: Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}

# Function with variable arguments and keyword arguments
def print_all_args(*args, **kwargs):
    print('Positional argument tuple:', args)
    print('Keyword arguments:', kwargs)
print_all_args(3, 2, 1, 'wait!', 'uh...', wine='merlot', entree='mutton', dessert='macaroon')
# Output: Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')
#         Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}

# Function with docstring
def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

print_if_true('Rumplestiltskin', True) # Output: Rumplestiltskin

# Function annotations
def annotated(a: int, b: int) -> int:
    return a + b

print(annotated(1, 2)) # Output: 3

# Function annotations with default arguments
def annotated(a: int, b: int = 1) -> int:
    return a + b

print(annotated(1)) # Output: 2

# Function annotations with variable arguments
def annotated(*args: int) -> int:
    return args

print(annotated(1, 2, 3)) # Output: (1, 2, 3)

# Function annotations with variable keyword arguments
def annotated(**kwargs: int) -> int:
    return kwargs

print(annotated(a=1, b=2, c=3)) # Output: {'a': 1, 'b': 2, 'c': 3}

# Function annotations with variable arguments and keyword arguments
def annotated(*args: int, **kwargs: int) -> int:
    return args, kwargs

print(annotated(1, 2, 3, a=1, b=2, c=3)) # Output: ((1, 2, 3), {'a': 1, 'b': 2, 'c': 3})

