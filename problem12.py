from common import divisor_count, primes_to_n

LIMIT = 1000000
primes = primes_to_n(LIMIT)

for i in xrange(1, LIMIT * 2):
    n = (i * (i + 1)) / 2
    divisors = divisor_count(n, primes) + 1

    if divisors > 500:
        print n
        break
