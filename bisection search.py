x = 23
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
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
