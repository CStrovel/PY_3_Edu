# Author: Charles Strovel
# this program  is a pica centro game example 

# Use variables to store table formatting information
# Declaring them as globals makes them easier to maintain
# if we wish to change how they look 
# HTABLEBREAK is the line between each row of the table 
HTABLEBREAK = "+-------------------+---------+-----------+"
# TABLEDATA is a preformatted string for storing data in the table
# can be used for headers or actual game data 
TABLEDATA = "| {GUESS:<18}| {PICA:<8}| {CENTRO:<10}|" 
# TABLEHEAD concantinates TABLEDATA between two HTABLEBREAKS
# for the purposes of printing a table header 
TABLEHEAD = HTABLEBREAK + "\n" + TABLEDATA + "\n" +HTABLEBREAK
# TABLEBODY is a concantinted string for displaying game data 
TABLEBODY = TABLEDATA + "\n" + HTABLEBREAK

# secret number  
digOne = 0
digTwo = 0
digThree = 0 

# flag variables
# these get set as the first, second and third
# is truthfully evaluated as either a pica or 
# centro to prevent duplicate evaluations 
picaOne = False
picaTwo = False
picaThree = False

centroOne = False
centroTwo = False
centroThree = False

def main():
    # guess variables 
    guessDigOne = 0
    guessDigTwo = 0
    guessDigThree = 0

    # global variables
    global centroOne 
    global centroTwo
    global centroThree

    # loop control variable 
    numGuesses = 10

    # get the secret number from the first user
    # then clear the screen
    setSecretNum()
    clearScreen()

    # begin the main loop
    # we will use a while loop as we are not sure
    # when the game state will end 
    while numGuesses > 0 and totalCentros() != 3:
        # ensure all flags are reset to 0 
        resetFlags() 

        # display how many more guesses the player has
        print("Guess #{:0>2}".format((11 - numGuesses)))

        # get the players guess digits  
        guessDigOne = getNumber("first", "guess")
        guessDigTwo = getNumber("Second", "guess")
        guessDigThree = getNumber("Third", "guess")

        # compare guesses for centros, setting centroOne
        # two and three accordingly to avoid duplicate counters
        if guessDigOne == digOne:
            centroOne = True

        if guessDigTwo == digTwo:
            centroTwo = True

        if guessDigThree == digThree:
            centroThree = True 

        # compare guesses for picas, if a guess has already been
        # found to be a centro, do not count it
        if not centroOne:
            isPica(guessDigOne)

        if not centroTwo:
            isPica(guessDigTwo)

        if not centroThree:
            isPica(guessDigThree)

        # display the current round of the game in table
        display(combineNumbers(guessDigOne, guessDigTwo, guessDigThree), totalPicas(), totalCentros())

        #decrement loop counter 
        numGuesses -= 1 

    # end the game 
    gameEnd(totalCentros())

    #input to hold screen
    input("\n press any key to return to console")

def setSecretNum():
    """This is function gets a secret three digit number from the user.
    This number is broken out from main() to prevent main()
    from being able to modify globals directly"""
    # we need to declare variables in global scope
    # we can combine this with getNumber to save on lines
    global digOne
    global digTwo  
    global digThree

    # set each digit with user input 
    digOne = getNumber("first","number")
    digTwo = getNumber("second","number")
    digThree = getNumber("third","number")

def getNumber(digString, numType):
    """This fucntion prompts for and returns digit input from the user"""

    return eval(input("Please enter the {} digit in your {}\t: ".format(digString, numType)))

# Function to clear the screen 
def clearScreen():
    clear = "\n" * 100
    print(clear)

def isPica(number):
    """This function will set the apporirate pica flag so the same 
    secret digit is not counted twice"""
    # we need to get the global variables first
    global picaOne
    global picaTwo
    global picaThree 
    
    # we do not want to accidently change the secret number
    # so it's safer to use digOne, two and three without
    # global scope applied 

    # begin comparing passed number to digits
    # we need to ensure that a single guessed digit
    # will not count twice in a secret number in which
    # that digit is repeated. We also need to ensure
    # centro digits are not recounted 
    if not picaOne and not centroOne and number == digOne:
        picaOne = True 

    elif not picaTwo and not centroTwo and number == digTwo:
        picaTwo = True 

    elif not picaThree and not centroThree and number == digThree:
        picaThree = True 

def totalPicas():
    """This function totals the number of picas currently
    flagged"""
    # declare variables
    picaCounter = 0

    # check for pica flags
    if picaOne:
        picaCounter += 1 
    
    if picaTwo: 
        picaCounter += 1 
    
    if picaThree:
        picaCounter += 1

    return picaCounter

def totalCentros():
    """This function totals the number of centros currently
    flagged"""

    # declare variables
    centroCounter = 0

    # check for centro flags
    if centroOne:
        centroCounter += 1 
    
    if centroTwo: 
        centroCounter += 1 
    
    if centroThree:
        centroCounter += 1

    return centroCounter

def combineNumbers(one, two, three):
    """This function will return a string that combines the
    three numbers that are passed to it"""

    return "{} {} {}".format(one,two,three)

def display(guessNum, numPicas, numCentros):
    """This function displays a table header and information about
    the current guess and number of picas/centros in that guess"""

    # We do not need to get the global variables 
    # as we do not want to modify them
    
    # print the top part of the table with colum labels 
    # using the global template 
    print(TABLEHEAD.format(GUESS = "YOUR GUESS", PICA = "PICA", CENTRO = "CENTRO"))
    # print the bottom part of the table with game data 
    # using the global template 
    print(TABLEBODY.format(GUESS = guessNum, PICA = numPicas, CENTRO = numCentros))

def resetFlags():
    """This function resets all global flags to 0"""
    # get global variables
    global picaOne
    global picaTwo
    global picaThree
    global centroOne 
    global centroTwo
    global centroThree

    picaOne = False
    picaTwo = False
    picaThree = False

    centroOne = False
    centroTwo = False
    centroThree = False

def gameEnd(centros):
    """ This function determines if the user has won or lost
    displaying an appropriate message"""
    if(centros == 3):
        print("Congratulations, you have guessed the secret number!")
    
    else:
        print("Unforunatly you have not managed to guess the secret number.")
        print("Better luck next time!")

    print("The secret number was {}".format(combineNumbers(digOne, digTwo, digThree)))

main()
