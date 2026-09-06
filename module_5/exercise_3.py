numbers = []

while True:
    user_input = input("Enter a number : ")  
    if user_input == "":
        break    
    numbers.append(float(user_input))
if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    
    print(f"\nSmallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")