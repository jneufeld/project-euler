one_to_nine = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    }

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    }

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    }

def get_word(n):
    result = ''

    if n < 1:
        pass
    elif n < 10:
        result += one_to_nine[n]
    elif n >= 10 and n < 20:
        result += teens[n]
    elif n >= 20 and n < 100:
        ten = n / 10
        one = n % 10

        result += tens[ten] + ' ' + one_to_nine[one]
    elif n >= 100 and n < 1000:
        hundred = n / 100
        ten = n % 100

        result += one_to_nine[hundred] + ' hundred'

        ten_word = get_word(ten)
        if ten_word != '':
            result += ' and ' + ten_word
    elif n > 999:
        result += 'one thousand'

    return result

words = ''
for n in xrange(1, 1000 + 1):
    words += get_word(n) + '\n'

words = words.split()
letters = 0

for word in words:
    letters += len(word)

print letters
