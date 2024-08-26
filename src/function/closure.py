# Closures are a way to keep the state of a function with the function itself.
# This is useful when you want to keep the state of a function between calls.

# This is a simple example of a closure that keeps the state of a counter.
# The counter is incremented by 1 each time the function is called.
# The counter is initialized to 0 when the function is created.
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Create a counter function
c = counter()

# Call the counter function
print(c()) # Output: 1

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a()) # Output: We are the knights who say: 'Duck'
print(b()) # Output: We are the knights who say: 'Hasenpfeffer'

