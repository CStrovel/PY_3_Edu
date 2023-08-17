# Author: Charles Strovel
# Description: This program demonstrates a basic technique for creating a
#              multi-dimensional list.
 
def main():
    # In Python, a list can consist of any of the basic data types.  A
    # multi-dimensional list can be created by making a list whose
    # individual elements are also lists.  Since there is no way to
    # explicitely declare a variable of any type, the best way to set up
    # a multi-dimension array is to write a function that creates the array.

    # upfront, we will decide the number of rows and the number
    # of columns in the list. Lets create a chess board for this example.
    num_rows = 8
    num_cols = 8

    # we will pass these parameters to a function that sets up an empty
    # multi-dimensioan list with nothing in it
    my2dList = Create2DList(num_rows, num_cols)

    # display the list
    displayBoard(my2dList)

    # from here, lets load up the list with starting piece positions 
    # remember that lists, by default, are passed by refference 
    startingPieces(my2dList)

    # display the loaded list
    print("\n") 
    displayBoard(my2dList)

def Create2DList(rows, cols):
    """ Creates a blank 2d list """ 
    # start with an empty 1D list
    returnList = []

    # generate the first dimension of indexes (rows)
    for x in range(rows):
        returnList.append([])

    # generate the second dimension of indexes (cols)
    for x in range(rows):
        for y in range(cols): 
            returnList[x].append(None) 

    # return the generated list
    return returnList

def startingPieces(my2dList): 
    """ Loads a 2D list representing a chess board with pieces """
    
    # List of capital pieces
    capPieces = ["Ro","Kn","Bi","Qu","Ki","Bi","Kn","Ro"] 

    # these two for loops are responsible for iterating thorugh the 
    # two dimensions of the list. 
    for x in range( len(my2dList) ): # Move through each item in lower list
        for y in range( len(my2dList[x]) ): # move through each item of of the list at my2dList[x]

            if x == 0 or x == len(my2dList) - 1: # check for first and last row of board 
                # if row is first or last, load with capital pieces 
                my2dList[x][y] = capPieces[y]

            elif x == 1 or x == len(my2dList) - 2: # check for pawn rows
                # If it is a pawn row, load with pawns
                my2dList[x][y] = "Pa"

            else: # all other positions can be blank 
                my2dList[x][y] = "  " 
    
def displayBoard(board):
    """simple loop to print the contents of a 2d list logically"""
    
    # move through all of the first dimension indexes in the 2d list
    for x in range( len(board) ):
        # we could spice up the presentation a bit more with a second loop
        # but just printing works for now
        print(board[x])
        print("")

# Begin MAIN()
main()
