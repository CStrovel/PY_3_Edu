# Author: Mark Dencler
# Modified for python 3.7 by Charles Strovel
# Description: This program demonstrates nested loops by drawing a
#              dynamic multiplication table.

def main():
    """ Gets column and row numbers from user, than handles call to make a multiplcation table"""

    # prompt the user for entries
    rows = eval(input("How many rows should draw: "))
    columns = eval(input("How many columns should draw: "))

    # draw the table with a function call
    drawMultiplicationTable(rows, columns)

def drawMultiplicationTable(rows, columns):
    """ Handles the nested loops to draw a multiplication table """ 

    # draw the top line of the table.
    # Since we are going to print a line across the table for every row, it makes sense to 
    # move this to a seperate function, so we only have to write the print loop once! 
    splitter(columns)

    # DRAW COLUMN HEADINGS
    # upper-left space
    print( '    |', end = "")
    for x in range(1, columns + 1):
        print ('{:^4}|'.format(x) , end = "")

    # draw a newline
    print('') 
    splitter(columns)


    # DRAW MAIN TABLE CONTENTS
    for x in range(1, rows + 1):    
        # draw each row heading
        print('{:^4}|'.format(x), end = "")

        for y in range(1, columns + 1):
            print('{:^4}|'.format(x * y), end = "")
        
        # draw our splitter row again 
        print('')
        splitter(columns)

def splitter(columns):
    """ draws a line across the table between each row """

    # the variable _ is often used in the case where we do not intend to actually
    # make use of it.
    for _ in range(1, columns + 2):  # goto 2 to fill upper-left space
        print('----+', end = "")
    print('')

# Begin MAIN()
main()
