low = 0
high = 100
mid = (low + high) // 2
guess = ' '

print('Please think of a number between 1 and 100!')

while guess != 'c':
    print('Is your secret number ' + str(int(mid)) + '?')
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess == 'h':
        high = mid
        mid = (low + high) // 2
    elif guess == 'l':
        low = mid
        mid = (low + high) // 2
    elif guess != 'h' and guess != 'l' and guess != 'c':
        print('I do not understand your input.')

print('Game over. Your secret number was ' + str(int(mid)))
