import random

random_numbers = random.randint(1, 10)

while True: 
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < random_numbers:
        print("Too low")
    elif user_guess > random_numbers:
        print("Too high")
    else:
        print("Correct!")
        break
