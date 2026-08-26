inches = float(input("Enter a value in inches: "))
while inches > 0:
    if inches >= 0:
        centimeters = inches * 2.54
        print(f"{inches} inches is equal to {centimeters} centimeters.")
        inches = float(input("Enter a value in inches: "))