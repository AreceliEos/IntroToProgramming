import random as r
import time as t
import sys as s
        
#constants
firstReel = None
secondReel = None
thirdReel = None

def accessMainMenu():
    print("Welcome to the Virtual Slot Machine v0.1!\n")
    response = str(input("Would you like to play? Please enter yes or no: \n"))
    if response == 'no':
        print("Thank you for stopping in! Good bye!")
        s.exit()
    else:
        print()
        #guest instructions
        print('''In order to win the amount listed, you must obtain the following combinations:\n
        ORANGE-ORANGE-ORANGE: wins $100
        WATERMELON-WATERMELON-WATERMELON: wins $75
        BANANA-BANANA-BANANA: wins $30
        7-7-7: wins the Jackpot!\n
        Winnings may vary on the amount of coins deposited.\n
        Guests are provided a $25 balance to start. Good Luck!\n''')
        t.sleep(5)

initialStake = int(input("Please deposit 1,2, or 3 coins to place bet: "))
initialBalance = 25
stake = initialStake
balance = initialBalance

def guestPrompt():#prompts guest if they wish to play again #while loop implemented
    while(True):
        answer = input("Guest has $" + str(stake) + " remaining. Play again?: \n")
        answer = answer.lower()
        if answer.lower() in ['yes']:
            return True
        else:
            print("Guest left slot machine with $", str(stake), "remaining.")
            s.exit()

def depositMoney(): #prompts user to insert coins to continue playing
    deposit = int(input("Please deposit 1, 2, or 3 coins to play: "))
    return deposit

def spinReel():
    #returns a random item from the items list
    items = ["ORANGE", "WATERMELON", "BANANA", "7"]
    randomItem = r.choice(items)
    return randomItem

def printWinnings():
    #presents guest with current winnings and balances
    if((firstReel == 'BANANA') and (secondReel == 'BANANA') and (thirdReel == 'BANANA')):
        win = 30
        totalBalance = balance - 30
    elif((firstReel == 'WATERMELON') and (secondReel == 'WATERMELON') and (thirdReel == 'WATERMELON')):
        win = 75
        totalBalance = balance - 75
    elif((firstReel == 'ORANGE') and (secondReel == 'ORANGE') and (thirdReel == 'ORANGE')):
        win = 100
        totalBalance = balance - 100
    elif((firstReel == '7') and (secondReel == '7') and (thirdReel == '7')):
        win = balance
        totalBalance = balance - win
    else:
        win = -1
        totalBalance = balance + 1
        
    if win == balance:
        print("You won the Jackpot!")
    if (win > 0):
        print(firstReel,'\t',secondReel,'\t',thirdReel,"-- Guest won $", str(win))
    else:
        print(firstReel,'\t',secondReel,'\t',thirdReel, "-- Guest lost")

def playSlotMachine():
    systemPrompt = accessMainMenu()
    guestResponse = guestPrompt()
    wager = depositMoney()
    while(stake != str(stake) and guestPrompt == True):
        firstReel = spinReel()
        secondReel = spinReel()
        thirdReel = spinReel()
        printWinnings()
        guestResponse = guestPrompt()
        wager = depositMoney()

playSlotMachine()
