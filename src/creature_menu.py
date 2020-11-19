def welcome():
    print("Welcome to the area computation tool!\n")
    print("**** MENU ****\n")
    print("Yeti     Compute probability of Yeti")
    print("Dragon   Compute probability of Dragon")
    print("Bigfoot  Compute probability of Bigfoot")
    print("Quit     Quit the tool\n")

def get_input():
    choice = input("Enter your choice: ")
    if(choice == "yeti"):
        return 'yeti'
    elif(choice == "dragon"):
        return 'dragon'
    elif(choice == "bigfoot"):
        return 'bigfoot'
    elif(choice == "quit"):
        quit()
    else:
        print(""+choice+" is an invalid choice, please enter valid choice now")
        return get_input()

def main():
    welcome()
    print("You chose: "+str(get_input()))

main()

