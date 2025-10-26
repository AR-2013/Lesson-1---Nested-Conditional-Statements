print("Hello! Welcome to ride.com! Please select your ride: ")
print("Option 1 is a car.")
print("Option 2 is a bike.")

choice = int(input("Select your choice - 1 or 2: "))

if(choice == 1):
    print("What type of car?")
    print("Option 1 is a Sedan.")
    print("Option 2 is a Rolls Voyce")

    choice2 = int(input(" Enter your second choice - option 1 or 2: "))
    if choice2 == 1: 
        print("You have selected a Sedan! Enjoy your ride!")
    else:
        print("You have selected a Rolls Voyce! Enjoy your ride!")
elif(choice == 2):
    print("What type of bike?")
    print("Option 1 is a scooty.")
    print("Option 1 is a scooter.")
    choice3 = int(input("Enter your choice - 1 or 2: "))

    if choice3 == 1:
        print("You have selected a scooty! Enjoy your ride!")
    else:
        print("You have selected a scooter! Enjoy your ride!")

else:
    print("Not a choice! Please choose again.")
