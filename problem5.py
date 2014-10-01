def div_by_all(num):
    result = True

    for divisor in xrange(2, 20 + 1):
        if num % divisor != 0:
            result = False
            break

    return result

for num in xrange(100, 9999999999):
    if div_by_all(num):
        print num
        break
