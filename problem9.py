MAX = 999

for a in xrange(1, MAX):
    for b in xrange(a, MAX):
        for c in xrange(b, MAX):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print a * b * c
