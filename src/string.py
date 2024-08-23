# Text String Manipulation Functions
print(str(5))
print(str(True))
print(str(3.14))
print(str(3 + 4j))
print(str([1, 2, 3]))
print(str((1, 2, 3)))
print(str({1, 2, 3}))
print(str({1: 2, 3: 4}))
print(str("hello"))
print(str(b"hello"))
print(str(bytearray(b"hello")))
print(str(memoryview(b"hello")))
print(str(None))

# Escape Sequences
palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
print(testimony)

speech = 'The backslash (\\) bends over backwards to please you.'
print(speech)

concatenate = 'Release the kraken! ' + 'No, wait!'
print(concatenate)

# String Formatting
print('hello'.format())
print('hello'.format_map({}))
print('hello'.format('world'))
print('hello'.format_map({'world': 'world'}))
print('hello {}'.format('world'))
print('hello {world}'.format(world='world'))

# String Constants
print(str.maketrans('abc', '123'))

# String Methods
print('hello'.capitalize())
print('hello'.center(10))
print('hello'.center(10, '*'))
print('hello'.count('l'))
print('hello'.endswith('o'))
print('hello'.startswith('h'))
print('hello'.find('l'))
print('hello'.index('l'))
print('hello'.isalnum())
print('hello'.isalpha())
print('hello'.isascii())
print('hello'.isdecimal())
print('hello'.isdigit())
print('hello'.isidentifier())
print('hello'.islower())
print('hello'.isnumeric())
print('hello'.isprintable())
print('hello'.isspace())
print('hello'.istitle())
print('hello'.isupper())
print('hello'.join(['a', 'b', 'c']))
print('hello'.ljust(10))
print('hello'.ljust(10, '*'))
print('hello'.lower())
print('hello'.upper())
print('hello'.title())
print('hello'.swapcase())
print('hello'.lstrip())
print('hello'.rstrip())
print('hello'.strip())
print('hello'.partition('e'))
print('hello'.rpartition('l'))
print('hello'.replace('l', 'L'))
print('hello'.rfind('l'))
print('hello'.rindex('l'))
print('hello'.rjust(10))


print('hello'.split('e'))
print(len('hello'))

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print(crypto_string)

print('hello'.zfill(10))

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())

