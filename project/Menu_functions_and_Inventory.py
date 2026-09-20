items = []


def add_item():
    item = input("Enter an item: ")
    items.append(item)
    print("Item added!")


def show_items():
    print("Items:")
    for item in items:
        print("-", item)


def clear_items():
    items.clear()
    print("All items have been removed.")


while True:
    print("\n--- GAME MENU ---")
    print("1. Add item")
    print("2. Show items")
    print("3. Clear items")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        show_items()

    elif choice == "3":
        clear_items()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")