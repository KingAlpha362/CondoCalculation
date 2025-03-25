print("Please enter your view choice:\n")

print("1: Park view ")

print("2: Golf course view: ")

print("3: Lake view:\n")

choice = int(input("Enter your choice from (1-3):\n"))
print("")

if choice == 1:
    price = 150000
    print(f"You chose {choice}, which is Park view and the price is ${price:,}")
elif choice == 2:
    price = 170000
    print(f"You chose {choice}, which is Golf course view and the price is ${price:,}")
elif choice == 3:
    price = 210000
    print(f"You chose {choice}, which is Lake view and the price is ${price:,}")
else:
    price = 0
    print("Invalid choice, try again.")

print(f"The final price is: ${price:,}\n")

if price > 0:
    print("Do you want a garage or a parking space:\n ")
    print("Garage you get charged extra $5000 plus condo view amount: ")
    print("Parking space has no charge")

parking_choice = int(input("Enter a number: (1-2):\n "))
print("")

if parking_choice == 1:
        price += 5000
        print("You selected a garage. Extra $5000 added.")
elif parking_choice == 2:
        print("You chose parking space. No charge.")
else:
        print("Invalid parking choice. Try again")

print(f"\nFinal price: {price:,}")