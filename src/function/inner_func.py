# Inner Functions Are Functions Defined Inside Other Functions

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7)) # Output: 11

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!')) # Output: We are the knights who say: 'Ni!'


