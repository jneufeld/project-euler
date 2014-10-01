TWO_DIGIT = 10
THREE_DIGIT = 100
FOUR_DIGIT = 1000

def is_palindrome(num):
    number = str(num)

    i, j = 0, len(number) - 1

    while i < j:
        if number[i] != number[j]:
            return False

        i += 1
        j -= 1

    return True

largest = -1

for i in xrange(THREE_DIGIT, FOUR_DIGIT):
    for j in xrange(THREE_DIGIT, FOUR_DIGIT):
        num = i * j

        if is_palindrome(num) and num > largest:
            largest = num 

print largest
