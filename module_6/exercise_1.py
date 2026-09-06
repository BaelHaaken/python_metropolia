import random

num_dice = int(input("How many dice to roll? "))

number = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i+1}: {roll}")
    number += roll

print(f"Sum of the dice: {number}")