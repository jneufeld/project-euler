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

primes_found, nth_prime = 0, 10001

for n in xrange(2, 99999999):
    if is_prime(n):
        primes_found += 1

    if primes_found == nth_prime:
        print n
        break
