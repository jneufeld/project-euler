def sum_of_squares(num):
    result = 0

    for x in xrange(1, num + 1):
        result += x * x

    return result

def square_of_sum(num):
    total = (num * (num + 1)) / 2
    return (total * total)

x = sum_of_squares(100)
y = square_of_sum(100)

print y - x
