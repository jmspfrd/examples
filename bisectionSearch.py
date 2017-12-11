x = 25
epsilon = 0.01 # deviation for the final answer. Must be within 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0 # in this case, 12

while abs(ans**2 - x) >= epsilon: # while the deviation is still above 0.01
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans # bring low up
    else:
        high = ans # bring high down
    ans = (high + low) / 2.0
print(' ')
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
print(' ')

#---------------------------------------------------------------

cube = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    print('guess**3 - cube = ' + str((guess**3 - cube)) + ' low = '
        + str(low) + ' high = ' + str(high) + ' guess = ' + str(guess))
    numGuesses += 1
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
print(' ')
print('numGuesses = ' + str(numGuesses))
print(str(guess) + ' is close to the cube root of ' + str(cube))
