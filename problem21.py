def get_divisors(n):
    result = []

    for d in xrange(1, (n / 2) + 1):
        if n % d == 0:
            result.append(d)

    return result

divisor_sum = {}
for n in xrange(2, 10000):
    divisors = get_divisors(n)
    divisor_sum[n] = sum(divisors)

amicable_pairs = set()
for num, count in divisor_sum.iteritems():
    if count in divisor_sum and divisor_sum[count] == num and num != count:
        amicable_pairs.add(num)
        amicable_pairs.add(count)

        print 'pair found: %d [%d] and %d [%d]' % (num,
            count,
            divisor_sum[num],
            divisor_sum[count])

total = 0
for num in amicable_pairs:
    total += num

print total
