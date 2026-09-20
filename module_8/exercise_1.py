def get_season(month):
    seasons = ("winter", "spring", "summer", "autumn")
    return seasons[month % 12 // 3]


month = int(input("Enter the number of a month (1-12): "))

if month < 1 or month > 12 :
    print ("You entered:", month)
    print ("Please enter a number between 1 and 12.")
else:
    season = get_season(month)
    print("You entered:", month)

    print(f"The season is {season}.")