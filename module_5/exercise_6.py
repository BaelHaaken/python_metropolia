import random

num_points = int(input("How many random points? "))

inside = 0
i = 0

while i < num_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        inside += 1

    i += 1

pi = 4 * inside / num_points

print("Approximation of pi:", pi)