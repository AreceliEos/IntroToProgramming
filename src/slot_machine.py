import random as r
import time as t
import sys as s

#constants
reel1 = r.choice(["ORANGE", "WATERMELON", "BANANA", "7"])
reel2 = r.choice(["ORANGE", "WATERMELON", "BANANA", "7"])
reel3 = r.choice(["ORANGE", "WATERMELON", "BANANA", "7"])
initialStake = 0
initialBalance = 25
stake = initialStake 
balance = initialBalance

def accessMainMenu():
    print("Welcome to the Virtual Slot Machine v0.1!")
    response =str(input("Would you like to start the machine? Please enter yes to pull the lever or no to exit: \n"))
    #if/else for user input
    if response == 'no':
        print("Thank you for stopping in! Good bye!")
        s.exit(0)
    else:
        print()
        #game instructions
        print('''In order to win the amount listed, you must obtain the following combinations:\n
        ORANGE-ORANGE-ORANGE: wins $100
        WATERMELON-WATERMELON-WATERMELON: wins $75
        BANANA-BANANA-BANANA: wins $30
        7-7-7: wins the Jackpot!\n
        Winnings may vary on the amount of coins deposited.\n
        Guests are provided a $25 balance to start. Good Luck!\n''')
        t.sleep(2)
        
def depositMoney(): #prompts user to insert coins
    deposit = int(input("Please deposit 1, 2, or 3 coins to play: "))    
    return deposit

def spinReel():
    #returns a random item from the items list
    items = ["ORANGE", "WATERMELON", "BANANA", "7"]
    randomItem = r.choice(items)
    return randomItem
    
def printWinnings():
    if((reel1 == 'BANANA') and (reel2 == 'BANANA') and (reel3 == 'BANANA')):
        win = 30 #winnings after each spin
        totalBalance = balance + win  #balance after each spin
    elif((reel1 == 'WATERMELON') and (reel2 == 'WATERMELON') and (reel3 == 'WATERMELON')):
        win = 75
        totalBalance = balance + win 
    elif((reel1 == 'ORANGE') and (reel2 == 'ORANGE') and (reel3 == 'ORANGE')):
        win = 100
        totalBalance = balance + win 
    elif((reel1 == '7') and (reel2 == '7') and (reel3 == '7')):
        win = 1000
        totalBalance = balance + win
    else:
        win = -1
        totalBalance = balance - 1
    
    if win == balance:
        print("You won the Jackpot!")
    if (win > 0):
        print(reel1,reel2,reel3,"-- You won $", str(win),"! Total balance $", totalBalance,'\n')
    else:
        print(reel1,reel2,reel3, "-- You lost. Total balance $", totalBalance,'\n')

def guestPrompt():#while loop implemented for user input #continue or quit options
    while True:
        print('Would you like to play again?')
        playAgain = str(input('Enter yes to continue or no to exit the machine: \n'))
        if playAgain == 'yes':
           play()
           print('\n')
        else:
            print('Thank you for stopping by! Come again soon!')
            s.exit(0)

def play():
    accessMainMenu()
    depositMoney()
    reel1 = spinReel()
    reel2 = spinReel()
    reel3 = spinReel()
    printWinnings()
    guestPrompt()
    
play()#runs the main menu #instructions #coin deposit #reel spins #winnings #continue/quit





  #thought process for altering bet  
     #if(depositMoney == 1):
        #wager = 10
        #totalBalance = balance + win + wager
   # elif(depositMoney == 2):
        #wager = 20
        #totalBalance = balance + win + wager
   # elif(depositMoney == 3):
        #wager = 30
        #totalBalance = balance + win + wager
   # else:
       # wager = 0
       # totalBalance = balance + win + wager
