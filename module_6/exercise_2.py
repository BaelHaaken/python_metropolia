numbers = []

while True:
    user_input = input("Enter a number: ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

if numbers:
    numbers.sort(reverse=True)
    top_five = numbers[:5]
    
    print("The greatest numbers in descending order:")
    for number in top_five:
        print(number)
else:
    print("No numbers were entered.")