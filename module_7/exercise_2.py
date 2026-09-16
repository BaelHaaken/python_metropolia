import random

def roll_dice(sides):
    return random.randint(1, sides)
    
number_of_sides = int(input("How many sides does the dice have?"))

while True:
    result = roll_dice(number_of_sides)
    print(result)
    
    if result == number_of_sides :
        break