def fact(n, fact_table={}):
    if n <= 1:
        return 1
    if n in fact_table:
        return fact_table[n]

    result = n * fact(n - 1)
    fact_table[n] = result

    return result

result = []

for i in xrange(3, 10000000):
    total = 0

    for digit in str(i):
        total += fact(int(digit))

    if total == i:
        result.append(i)

print result
print sum(result)
