import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input('Please choose an option: ')

    if(userChoice == "1"):
        print("What item do you want to add to the backpack?: ")
        itemToAdd = input()
        itemsInBackpack.append(itemToAdd) # adds last inputted value at end of the list
        # using append instead of insert function as to add an element of realism
        # i.e. last added item is most likely sitting at the top of your backpack when you open it

    if(userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?: ")
        itemToCheck = input()
        if itemToCheck in itemsInBackpack:
            print('This item is in your backpack.')
        elif itemToCheck not in itemsInBackpack:
            print('This item is not in your backpack.')

    if(userChoice == "3"):
        sys.exit('Thank you for checking your inventory.')
