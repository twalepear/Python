import random

response = "y"
while response.lower() == "y":
    user_choice = input('rock (r), paper (p), scissors (s)? ')
    choices = ('rock', 'paper', 'scissors')
    roll = random.choice(choices)
    print(roll)
    if user_choice == 'r' and roll == 'paper':
        print(f"you lose!")
    elif user_choice == 'r' and roll == 'scissors':
        print(f"you win!")
    elif user_choice == 'p' and roll == 'rock':
        print(f"you win!")
    elif user_choice == 'p' and roll == 'scissors':
        print(f"you lose!")
    elif user_choice == 's' and roll == 'rock':
        print(f"you lose!")
    elif user_choice == 's' and roll == 'paper':
        print(f"you win!")
    else:
        print(f"haha same")
    response = input("let's play again? (y/n): ")
