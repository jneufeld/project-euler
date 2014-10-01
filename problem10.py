import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for d in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % d == 0:
            return False

    return True

total = 0

for n in xrange(2, 2000000):
    if is_prime(n):
        total += n

print total
