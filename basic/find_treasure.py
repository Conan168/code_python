print("Welcome to Treasure Island! \n Your mission is to find a treasure.")
choice1 = input('You\'re at a cross road. which direction do you head to? Type "Left" or "Right" \n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is a island in the middle of island. '
                    'Type "swim" to swim across. '
                    'Type "wait" to wait a boat \n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve arrive island. '
                'There are three color door "red", "yellow" and "blue". '
                'which color do you choose. \n').lower()
        if choice3 == "red":
            print("Congradulation. You get a treature")
        elif choice3 == "yellow":
            print("Fire is full in the room!")
        elif choice3 == "blue":
            print("beast is full in the room!")
        else:
            print("the door is not exist. game over!")     
    else:
        print("you die because of monster")

else:
    print("You fell into hole and dead.") 
