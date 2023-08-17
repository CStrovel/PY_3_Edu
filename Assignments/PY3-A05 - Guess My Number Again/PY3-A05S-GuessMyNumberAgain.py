# Author: Charles Strovel
# Description: This program is example code for assignment 5
# guess my number game using loops and random number generation.
import random

def main():
    """ Provides main flow control for guess my number """

    # Declare variables
    secretNum = 0 # secret number, determined randomly  
    numGuesses = 0 # number of guesses left
    gameWin = False # has the player guessed correctly?
    lower = 0 # lower boundry for random number
    upper = 0 # upper boundry for random number

    # get difficulty level from user
    lower, upper, numGuesses = getDifficulty()

    # generate the secret number from previous user input
    # random.randint returns a random integer within the passed range 
    secretNum = random.randint(lower, upper)
    
    print("\nThe secret number has been generated... the game has begun.")

    # loop while the player has not run out of guesses and not won the game 
    while numGuesses != 0 and not gameWin:
        # Get the players guess, then evaluate it against the secret number
        gameWin = evaluateGuess(getGuess(numGuesses), secretNum)
        
        # decrment number of guesses left
        numGuesses -= 1 

    # Congradulate (or chastize) the user
    gameEnd(gameWin, secretNum)
    input()
    
def getDifficulty():
    """ Aquires a dificulty level from the user. Returns assocated game settings"""

    # Declare Variables 
    selection = 0 # begin at an invalid number
    difString = "{}.) {:8}(Number Range: {}-{:<7}; Guesses:{:3})" # string for difficulty formatting
    easyMin, easyMax, easyGuess = 1, 25, 5 # easy difficulty numbers
    medMin, medMax, medGuess = 1, 100, 8 # medium difficulty numbers
    hardMin, hardMax, hardGuess = 1, 1000, 12 # hard difficulty numbers 

    # check until the user provides a valid number 
    while selection != 1 and selection != 2 and selection != 3:
        print("Welcome To GUESS MY NUMBER... Please select a difficulty:")
        print(difString.format(1, "Easy", easyMin, easyMax, easyGuess))
        print(difString.format(2, "Medium", medMin, medMax, medGuess))
        print(difString.format(3, "Hard", hardMin, hardMax, hardGuess))
        selection = eval(input("Diffculty Level: "))

    if selection == 1: # return if easy
        return easyMin, easyMax, easyGuess
                         
    elif selection == 2:# return if medium
        return medMin, medMax, medGuess
                         
    else: # return if hard 
        return hardMin, hardMax, hardGuess

def getGuess(guessLeft):
    """ alerts the user to the guesses remaining, than returns user input"""
    # guesses left
    print("\nYou have {} guesses remaining".format(guessLeft))

    # get player input
    return eval(input("Take a guess at the secret number: "))

def evaluateGuess(guess, secret):
    """Evaluates first parameter reliative to second parameter

    Function provides feed back on if first parameter is less than
    greater than or equal to the second paramiter. Returns true
    if they are equal, otherwise returns false
    """
    # Declare variables 
    guessCorrect = False

    # Check if guess and secret are equal
    # provide feedback on greater than or
    # less than
    if guess == secret:
        guessCorrect = True
        feedback(guess, "equal to")
        
    elif guess > secret:
        feedback(guess, "less than")

    else: # there is only one case left 
        feedback(guess, "greater than")

    return guessCorrect
        
def feedback(number, relStr):
    """ Prints feedback string for evaluateGuess """

    print("The secret number is {} {}.".format(relStr, number))

def gameEnd(gameWin, secret):
    """ Produces a victory or defeat message for the user depending on gameWin """ 
    # if the user has won the game 
    if gameWin:
        print("\nCongratulations, the secret number was {}. Good Guessing!".format(secret))

    #otherwise the uesr has lost the game
    else:
        print("\nUnfortunatly you failed to guess the secret number in the allowed")
        print("number of guesses. The secret number was {}, better luck next time!".format(secret))

# main function call
main()

