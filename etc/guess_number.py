from random import random

number_to_guess = round(random() * 100)
user_try = 1
print("Computer got a number to guess")

while user_try <= 10:
    user_number = int(input('Try #{}: '.format(str(user_try))))
    if user_number > number_to_guess:
        print('Too much')
    elif user_number < number_to_guess:
        print('Too less')
    else:
        print('You have guessed from {} try'.format(user_try))
        break
    user_try += 1
else:
    print('You used all your 10 tries, were guessed: ', number_to_guess)