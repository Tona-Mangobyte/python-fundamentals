# Loop statement

count = 1
while count <= 5:
    print(count)
    count += 1

print("end!")

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
        print('No even number found')

for x in range(0,3):
    print(x)

print(list(range(0, 3)))
print(list(range(0, 11, 2)))
print(list(range(5, 0, -1)))

