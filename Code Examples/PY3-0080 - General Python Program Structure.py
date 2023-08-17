# Author: Mark Dencler
# edited for python 3.7 by: Charles Strovel 
# Description: This program demonstrates the basic function-based layout
# of a typical Python program.

# The first function that appears in any Python program is main()
def main():
    print('This is the first statement in main')
    #main will invoke functionOne()
    functionOne()
    #main will invoke functionTwo()
    functionTwo()

    #Pauses the program so output can be viewed
    input()

# After the main() function, the definitions for the other functions come.
def functionOne():
    print('This is the first statement in functionOne()')

def functionTwo():
    print('This is the first statement in functionTwo()')

# functions do not execute without being invoked (called), at the 
# end of the program a single statement needs to be inserted to get
# main() executing.
main()

    
