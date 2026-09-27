

from player import Player
from room import Room
from item import Item




sword = Item("Valyrian Steel Sword", 3.5)
dragon_egg = Item("Dragon Egg", 2.0)
crown = Item("King's Crown", 1.5)
gold = Item("Bag of Gold", 5.0)




entrance = Room("King's Landing Entrance")
throne_room = Room("Throne Room", crown)
dragon_room = Room("Dragon Room", dragon_egg)
armory = Room("Armory", sword)
treasury = Room("Royal Treasury", gold)



player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))




if player_age < 0:
    print("Invalid age. Age cannot be negative.")

elif player_age < 12:
    print("The player is a minor.")

else:
    print(f"\nWelcome, {player_name}!")
    print(f"You are {player_age} years old.")
    print("WELCOME TO KING'S LANDING")

    # Create the player
    player = Player(player_name, player_age, entrance)




    def show_items():
        print("\nItems:")

        if len(player.items) == 0:
            print("Your inventory is empty.")
        else:
            for item in player.items:
                print("-", item.name, "-", item.weight, "kg")


    def clear_items():
        player.clear_items()
        print("All items have been removed.")



    def move_player():
        print("\nWhere do you want to go?")
        print("1. King's Landing Entrance")
        print("2. Throne Room")
        print("3. Dragon Room")
        print("4. Armory")
        print("5. Royal Treasury")

        choice = input("Choose a room: ")

        if choice == "1":
            player.move(entrance)

        elif choice == "2":
            player.move(throne_room)

        elif choice == "3":
            player.move(dragon_room)

        elif choice == "4":
            player.move(armory)

        elif choice == "5":
            player.move(treasury)

        else:
            print("Invalid room.")
            return

        print("You moved to", player.location.name)

        if player.location.item is not None:
            print("There is an item here:", player.location.item.name)




    def collect_item():
        item = player.collect_item()

        if item is not None:
            print("You collected:", item.name)
        else:
            print("There is no item in this room.")


    def show_location():
        print("\nCurrent location:", player.location.name)

        if player.location.item is not None:
            print("There is an item here:", player.location.item.name)
        else:
            print("There is no item here.")



    while True:

        print("\n--- MAIN MENU ---")
        print("1. Show location")
        print("2. Move")
        print("3. Collect item")
        print("4. Show inventory")
        print("5. Clear inventory")
        print("6. Daemon")
        print("7. Caraxes")
        print("8. Daemon Tagaryen")
        print("9. Quit")

        player_command = input("Enter a command: ")


        if player_command == "1":
            show_location()


        elif player_command == "2":
            move_player()


        elif player_command == "3":
            collect_item()


        elif player_command == "4":
            show_items()


        elif player_command == "5":
            clear_items()


        elif player_command.lower() == "daemon":
            print("Daemon enters the room.")
            print("Aura +1000.")


        elif player_command.lower() == "caraxes":
            print("Caraxes has been summoned.")
            print("Aura +1000.")


        elif player_command.lower() == "daemon tagaryen":
            print("Daemon Tagaryen has arrived.")
            print("Aura +1000.")


        elif player_command == "9" or player_command.lower() == "lopeta":
            print("Goodbye!")
            break


        else:
            print("Invalid command.")