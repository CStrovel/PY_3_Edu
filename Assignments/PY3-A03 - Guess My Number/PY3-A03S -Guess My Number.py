#Written By Charles Strovel
#Python 3.7
#this program is a multiplayer guessing game
secretNum = 0
playerGuess = 0
winFlag = False

#function that gets a secret number from a user----------
#stores in a global variable-----------------------------
def getSecretNum():
    #get globals 
    global secretNum

    #get secret number from the user 
    secretNum = eval(input("Please enter a secret number: "))
    ClearScreen()

#function to retrieve player guess-----------------------
#stores in a global variable ----------------------------
def guess():
    #get globals 
    global playerGuess

    #get players guess
    playerGuess = eval(input("try to guess the secret number: "))

#function to compare player guess and secret number------
#calls numHint() or sets win flag------------------------
def compare(playerG, secretN):
    #get globals
    global winFlag 

    #determine state of win flag boolian 
    winFlag = playerGuess == secretNum

    #compare greater then or less then for hint 
    if playerG > secretN: 
        numHint("less", playerG)
    elif playerGuess < secretNum:
       numHint("greater", playerG)
        

#function that reads end winFlag to determine a winner---
#--------------------------------------------------------
def gameEnd(GLE, secretN):
    #check for game win flagged (0 in winFlag) and print appropriate message 
    if GLE:
        print("You Got It!")
        print("\nCongratulations... the secret number was {0:d}".format(secretN))
        print("You Win!!! Game Over")

    else:
        print("\nSorry, you were not able to guess the secret number")
        print("You lose. Game Over")
        print("\nThe secret number was {0:d} BTW. Better luck next time".format(secretN))

    input()

#function that provides a hint to player-----------------
#--------------------------------------------------------
def numHint(hintStr, playerGuess):
    print("The secret number is {0:s} than {1:d}\n".format(hintStr, playerGuess))

#function that clears the screen-------------------------
#--------------------------------------------------------
def ClearScreen():
     clear = "\n" * 100
     print(clear)

#Main flow control function------------------------------
#--------------------------------------------------------
def main():
    #get global variables 
    global playerGuess
    global secretNum 
    global winFlag

    #main function calls
    getSecretNum()
    #first guess round
    guess()
    compare(playerGuess, secretNum)
    #second guess round
    if not winFlag:
        guess()
        compare(playerGuess, secretNum)    
    #third guess round
    if not winFlag:
        guess()
        compare(playerGuess, secretNum)
    #fourth guess round
    if not winFlag:
        guess()
        compare(playerGuess, secretNum)
    #fifth guess round
    if not winFlag:
        guess()
        compare(playerGuess, secretNum)
    #determine a winner 
    gameEnd(winFlag, secretNum)

#start main control function 
main()
