# Anonymous Functions: lambda
# Lambda functions are small anonymous functions that can have any number of arguments, but can have only one expression.

# Syntax
# lambda arguments : expression

def edit_story(words, func):
    for word in words:
        print(func(word))

words = ['hello', 'world', 'python', 'is', 'awesome']
edit_story(words, lambda word: word.capitalize() + '!')


def enliven(word):
    return word.capitalize() + '!'
edit_story(words, enliven)
