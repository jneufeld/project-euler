a, b, i = 1, 1, 3
while True:
    a, b = b, a + b

    if len(str(b)) == 1000:
        print i
        break

    i += 1
