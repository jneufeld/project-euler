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

def is_cyclic_prime(n):
    num = str(n)

    for i in xrange(len(num) - 1):
        num = num[-1:] + num[:-1]
        if not is_prime(int(num)):
            return False

    return True
        
count = 0
for i in xrange(2, 1000000):
    if is_prime(i) and is_cyclic_prime(i):
        count += 1

print count
