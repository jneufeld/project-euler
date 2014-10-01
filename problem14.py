collatz_length = {}

def collatz(n):
    if n == 1:
        return 1

    if n in collatz_length:
        return collatz_length[n]
    if n % 2 == 0:
        result = 1 + collatz(n / 2)
        collatz_length[n] = result
        return result

    result = 1 + collatz((3 * n) + 1)
    collatz_length[n] = result
    return result

longest, number = 0, 0

for n in xrange(1, 1000000):
    length = collatz(n)

    if length > longest:
        longest = length
        number = n

print 'number=%d, length=%d' % (number, length)
