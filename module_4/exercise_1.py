zander_size = float(input("Enter the size of the zander (in cm): "))
if zander_size < 42:
    print(f"The zander is {42 - zander_size} cm below the size limit.")
else:
    print("The zander meets the size limit.")