numbers = set()

for a in xrange(2, 100 + 1):
    for b in xrange(2, 100 + 1):
        n = a ** b
        numbers.add(n)

print len(numbers)
