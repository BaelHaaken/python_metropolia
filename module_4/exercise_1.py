zander_size = float(input("Enter the length of the zander (in cm): "))
if zander_size < 42:
    print(f"The zander is {42 - zander_size} cm below the length limit.")
else:
    print("The zander meets the length limit.")