numbers = set()

for number in xrange(1, 1000):
    if number % 3 == 0:
        numbers.add(number)
    elif number % 5 == 0:
        numbers.add(number)

result = sum(numbers)

print result
