import random

response = "y"
while response.lower() == "y":
    user_choice = input('rock (r), paper (p), scissors (s)? ')
    choices = ('rock', 'paper', 'scissors')
    roll = random.choice(choices)
    they_lost = ('you lose!', 'haha', '😜', '😁')  # for emotes: Windows key + .
    they_won = ('you win!', 'nice one', '👍', '👏')
    draw = ('same!', 'haha same~', '🙌', '😂')
    print(roll)
    if user_choice == 'r' and roll == 'paper':
        print(f"{random.choice(they_lost)}")
    elif user_choice == 'r' and roll == 'scissors':
        print(f"{random.choice(they_won)}")
    elif user_choice == 'p' and roll == 'rock':
        print(f"{random.choice(they_won)}")
    elif user_choice == 'p' and roll == 'scissors':
        print(f"{random.choice(they_lost)}")
    elif user_choice == 's' and roll == 'rock':
        print(f"{random.choice(they_lost)}")
    elif user_choice == 's' and roll == 'paper':
        print(f"{random.choice(they_won)}")
    else:
        print(f"{random.choice(draw)}")
    response = input("let's play again? (y/n): ")
