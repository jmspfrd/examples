x = float(input('Enter an integer or a decimal between 0 and 1: '))
orig = x

# convert integers into binary
if float(x)%1 == 0.0:
    if int(x) < 0:
        isNeg = True
        x = abs(int(x))
    else:
        isNeg = False
    result = ''
    if int(x) == 0:
        result = '0'
    while int(x) > 0:
        result = str(int(x)%2) + result
        x = int(x) // 2
        print(result)
    print('The binary representation of the integer ' + str(int(orig)) + ' is ' + str(result))
    if isNeg:
        result = '-' + result


# convert fractions into binary
else:
    p = 0
    while ((2**p) * float(x)) % 1 != 0:
        print('Remainder = ' + str((2**p) * float(x) - int((2**p) * float(x) )))
        p += 1

    num = int(float(x) * (2**p))

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num//2

    for i in range(p - len(result)):
        result = '0' + result

    result = result[0:-p] + '.' + result[-p:]
    print('The binary representation of the decimal ' + str(float(x)) + ' is ' + str(result))
