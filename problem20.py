def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

x = factorial(100)
total = 0

for digit in str(x):
    total += int(digit)

print total
