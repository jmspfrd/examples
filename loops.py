"""

x = int(input('Enter an integer: '))
ans = 0

while ans ** 3 < abs(x):
    ans += 1
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube.')
else:
    if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))



cube = int(input('Enter an integer: '))

for guess in range(abs(cube + 1)):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, ' is not a perfect cube.')
else:
    if cube < 0:
        guess = - guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))



iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1


for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break



s = 'aaaaarrrro'
count = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1

print('Number of vowels: ' + str(count))



# finds #s of 'bob' in a string

s = 'azcbobobegghakl'
count = 0
start = 0
stop = 3

for i in s:
    sl = slice(start,stop)
    if s[sl] == 'bob':
        count += 1
    start += 1
    stop += 1
    print(s[sl])

print('Number of times bob occurs is: ' + str(count))

"""

s = 'qroponmlkjihgfedcbab'
#s = 'abcdefghijklmnopqrstuvwxyz'

substring = s[slice(0, 1)]
start = 0
stop = 1
ans = s[slice(0, 1)]
ans2 = s[slice(0, 1)]

for i in range(len(s)-1):
    firstLetter = s[slice(start, stop)]
    lastLetter = s[slice(start + 1, stop + 1)]

    if firstLetter <= lastLetter:
        start += 1
        stop += 1
        substring += lastLetter
        if len(substring) > len(ans):
            ans = substring

    elif firstLetter > lastLetter:
        start += 1
        stop += 1
        substring = lastLetter
        if len(substring) > len(ans):
            ans2 = substring

if len(ans) >= len(ans2):
    print('Longest substring in alphabetical order is: ' + ans)
elif len(ans2) > len(ans):
    print('Longest substring in alphabetical order is: ' + ans2)
