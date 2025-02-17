name = input("Hey type your name: ")
print(f"Hello {name} welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!")
    weapon = input("Choose a weapon (sword/axe) ").lower()

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print(" You went left and fell of  cliff.You are dead!")
    
    elif direction == "right":
        choice = input("you now see a bridge, do you want to swim under it or cross it? (swim/cross)").lower()
        if choice == "swim" and weapon == "axe":
            print("You defeated  an alligator and crossed successfully! ")
        elif choice == "cross" and weapon == "sword":
            print("You encountered a guardian and defeated them")
        else:
            print("You died!,the end")

    else:
        print("Sorry not a valid reply, you die!")


else:
    print("We are NOT playing...")


