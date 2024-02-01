import random

user_choice = input('Rock (r), Paper (p), Scissors (s)? ')
choices = ('rock', 'paper', 'scissors')
roll = random.choice(choices)

print(roll)
if user_choice == 'r' and roll == 'paper':
    print("you lose!")
elif user_choice == 'r' and roll == 'scissors':
    print("you win!")
elif user_choice == 'p' and roll == 'rock':
    print("you win!")
elif user_choice == 'p' and roll == 'scissors':
    print("you lose!")
elif user_choice == 's' and roll == 'rock':
    print("you lose!")
elif user_choice == 's' and roll == 'paper':
    print("you win!")
else:
    print("let's play again?")
