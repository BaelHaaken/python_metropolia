player_age = int(input("Enter the player's age: "))
if player_age < 0:
    print("Invalid age. Age cannot be negative.")
elif player_age < 12:
    print("The player is a minor.")
else:
    print("Welcome to King's Landing!")

while True:
    print ("Main Menu:")
    correct_player_commands = "lopeta"
    player_commands = input("Enter a command: ")

    daemon_tagaryan_commands = ["daemon", "caraxes", "daemon tagaryen"]
    if player_commands.lower() in daemon_tagaryan_commands:
        print("Aura +1000.")