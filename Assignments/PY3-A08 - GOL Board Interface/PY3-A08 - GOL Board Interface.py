# Globals
INPUT_FILE = 'A08S-GOLBoardInterfaceData.dat'
EMPTY = 0 
ROW_NUM = 10
COL_NUM = 10
MARK_DEATH = 'D'
MARK_LIVE = 'L'


def create2Darray(row,column):
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

def main():
    # Build the board 
    board = create2Darray(ROW_NUM, COL_NUM)
    # Set the board to all death markers 
    board = intializeBoard(board, MARK_DEATH)
    # Insert live markers  
    board = populateBoardFromFile(board, INPUT_FILE, MARK_LIVE)
    # i will become the loop index for the full GOL program 
    i = 0 
    # Display the board 
    display(board, i)
main()