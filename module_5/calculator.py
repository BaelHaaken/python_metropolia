menu = ("Menu: \n1. Add\n2. Minus\n3. Multiply\n0. Exit\nChoose an option (0-3): ")
selection = (input(menu))
while selection != "0":
    if selection == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Result: {result}")
        menu = ("Menu: \n1. Add\n2. Minus\n3. Multiply\n0. Exit\nChoose an option (0-3): ")
        selection = (input(menu))
    elif selection == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"Result: {result}")
        menu = ("Menu: \n1. Add\n2. Minus\n3. Multiply\n0. Exit\nChoose an option (0-3): ")
        selection = (input(menu))
    elif selection == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Result: {result}")
        menu = ("Menu: \n1. Add\n2. Minus\n3. Multiply\n0. Exit\nChoose an option (0-3): ")
        selection = (input(menu))
    elif selection != "0" and selection != "1" and selection != "2" and selection != "3":
        print("Invalid option. Please choose a valid option (0-3).")
        menu = ("Menu: \n1. Add\n2. Minus\n3. Multiply\n0. Exit\nChoose an option (0-3): ")
        selection = (input(menu))
if selection == "0":
    print("Exiting the program.")
