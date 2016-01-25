print "Please think of a number between 0 and 100!"
user_input = ''
low = 0
high = 100
guess = (high + low) / 2

while user_input != 'c':
    print "Is your secret number {}?".format(guess)

    user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly. ")

    if user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    elif user_input == 'c':
        print "Game over. Your secret number was:", guess
        break
    else:
        print "Sorry, I did not understand your input"
        continue

    guess = (high + low) / 2
