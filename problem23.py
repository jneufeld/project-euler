LIMIT = 28123

def get_divisors(n):
    result = []

    for d in xrange(1, (n / 2) + 1):
        if n % d == 0:
            result.append(d)

    return result

def is_abundant(n):
    result = False

    divisors = get_divisors(n)
    divisor_sum = sum(divisors)

    if divisor_sum > n:
        result = True

    return result   

abundant_numbers = []
for n in xrange(2, LIMIT):
    if is_abundant(n):
        abundant_numbers.append(n)

abundant_sums = set()
for a in abundant_numbers:
    for b in abundant_numbers:
        total = a + b

        if total > LIMIT:
            continue

        abundant_sums.add(total)

total = 0
for num in xrange(1, LIMIT + 1):
    if num not in abundant_sums:
        total += num

print total
