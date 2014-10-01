numbers = []

for i in xrange(2, 5000000):
    number = str(i)
    total = 0

    for digit in number:
        total += int(digit) ** 5

    if i == total:
        numbers.append(i)

print sum(numbers)
