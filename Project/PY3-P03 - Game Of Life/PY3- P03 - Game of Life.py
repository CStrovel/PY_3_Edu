# Author: Charles Strovel
# Descrption: Program impliments conways game of life on a 2D grid 
# Globals
INPUT_FILE = 'P03S-StartingState.dat'
EMPTY = 0 
ROW_NUM = 10
COL_NUM = 10
MARK_DEATH = ' '
MARK_LIVE = '*'


def create2Dlist(row,column):
    """Creates an empty 2 dimensional array of dimension row x column"""
    # Variables 
    rtrnLst = []

    for i in range(row):
        # Create a new list at the next location in rtrnLst
        rtrnLst.append([])

        for _ in range(column):
            # Append column # of EMPTY spaces into current rtrnLst row
            rtrnLst[i].append(EMPTY)
    
    return rtrnLst

def intializeBoard(gameBoard, fillChar):
    """Fills a 2D array with the specified character"""
    # loop through rows
    for row in gameBoard:
        # loop through each column and assign character 
        for i in range(len(row)):
            row[i] = fillChar

    return gameBoard 

def populateBoardFromFile(gameBoard, inputFile, fillChar):
    """Fills a 2D array with specified character at locations specified by file"""
    # variables 
    valid = True 

    # open input file using with method 
    with open(inputFile, 'r') as fileHandle: 
        # Iterate through the lines in the file 
        for line in fileHandle:
            # set validation flag to true 
            valid = True 

            # strip new lines and split into cordinates 
            xCoord, yCoord = line.strip("\n").split(" ")
            
            # try converting coord values to integers   
            try:
                xCoord = int(xCoord)

            except: 
                print("Invalid data found in line {} {}. Discarding line.".format(xCoord, yCoord))
                valid = False 

            try: 
                yCoord = int(yCoord) 
            
            except: 
                print("Invalid data found in line {} {}. Discarding line.".format(xCoord, yCoord))
                valid = False 

            # if cordinants are integers attempt to fill board space 
            if valid: 
                try:
                    gameBoard[xCoord][yCoord] = fillChar

                except:
                    print("The coordinate for line {} {} can not be accessed on the board.".format(xCoord, yCoord))
    
    return gameBoard 

def display(gameBoard, genNumber):
    """Displays a 2D list with title and presentation formatting """
    # Generation title
    print("+{:-<20}+".format(""))
    print("| {:<19}|".format("Generation: " + str(genNumber)))
    print("+{:-<20}+".format(""))
    
    # print top divider 
    print("+---" * len(gameBoard[0]) + "+")
    
    # loop through rows
    for row in gameBoard:
        #loop through individual columns 
        for column in row:
            print("| " + str(column) + " ", end = "")
        
        # new line 
        print("|")
        # horizontal divider 
        print("+---" * len(row) + "+")

def generationShift(board, markDead, markAlive):
    """Handles the change of board state for each generation"""
    # Get a clean duplicate board so that changes 
    # between generations do not collide
    newBoard = intializeBoard(create2Dlist(len(board),len(board[0])), markDead)
    # iterate through each row of the board
    for row in range( len(board) ):
        # iterate through each column of the board 
        for column in range( len(board[row]) ):
            # for each cell, total the number of live neighbors 
            totalNeighbors = getTotalNeighbors(board, row, column, markAlive)
            # check if the cell should be alive. dead cells are already 
            # filled in from intializing the board, so we only need to check for
            # which cells should be alive 
            if board[row][column] == markAlive and totalNeighbors == 2 or totalNeighbors == 3:
                # assign living cell into new board 
                newBoard[row][column] = markAlive

            elif board[row][column] == markDead and totalNeighbors == 3:
                # assign living cell for new board
                newBoard[row][column] = markAlive 

    return newBoard   

def getTotalNeighbors(board, row, column, markAlive):
    """Totals the number of neighbors a cell has"""
    # Variables
    counter = 0

    # check row above current cell location 
    counter += checkCell(board, row - 1, column - 1, markAlive)
    counter += checkCell(board, row - 1, column, markAlive)
    counter += checkCell(board, row - 1, column + 1, markAlive)

    # check current row 
    counter += checkCell(board, row, column - 1, markAlive)
    counter += checkCell(board, row, column + 1, markAlive)

    # check row below current cell location 
    counter += checkCell(board, row + 1, column - 1, markAlive)
    counter += checkCell(board, row + 1, column, markAlive)
    counter += checkCell(board, row + 1, column + 1, markAlive)
    
    return counter

def checkCell(board, row, column, markAlive):
    """Checks if a cell is living or dead, returns a 1 if yes, 0 if no"""
    # variables 
    isLiving = 0
    # check if the cell is alive, change flag to 1 if true
    # a try block allows us to ignore out of range array indexs
    try:
        if board[row][column] == markAlive:
            isLiving = 1 

    # exception if the array index is out of bounds (off board edge)
    except IndexError:
        isLiving = 0

    return isLiving

def getGens():
    """gets the generation count from the user, parsing it for an intenger"""
    # variables
    goodGen = False

    while not goodGen:
        # set flag to true, we will try to convert to an integer and set the
        # flag accordingly later 
        goodGen = True 
        genNumber = input("Please enter the number of generations to run:")

        try:
            # attempt to convert the value to something useful
            genNumber = abs(int(genNumber))
        
        # re iterate the while loop until the user inputs valid data
        except:
            print("invalid generation number.")
            goodGen = False
    
    return genNumber 

def main():
    """Handles main control flow for program"""
    # Build the board 
    board = create2Dlist(ROW_NUM, COL_NUM)
    # Set the board to all death markers 
    board = intializeBoard(board, MARK_DEATH)
    # Insert live markers  
    board = populateBoardFromFile(board, INPUT_FILE, MARK_LIVE)
    # get # of generations to run from user 
    genNumber = getGens()
    # loop through the remainder of the generations
    for i in range(genNumber):
        # display the results
        display(board, i)
        # run through a generation
        board = generationShift(board, MARK_DEATH, MARK_LIVE)


main()