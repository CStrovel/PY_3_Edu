# Author: Charles Strovel 
# Description: This program demonstrates while loops.

def main():
    whileLoop()
    userLoop()
    userBoolLoop()

def whileLoop():
    """ Loops will continue executing the code block nested
     within them until the condition they are checking is
     no longer true. While loops have no means of automaticly
     incrimenting or decrimenting a counter. The counter must
     be incrimented or decrimented within the body of the loop.""" 
    print("\n{:*^70}".format("Basic While Loop"))
    
    x = 1 # a variable a loop is checking must be intialized 
    
    while x <= 5: # start of loop
        # everything within the loops body should be lined up
        # one more tab right of the start of the loop 
        print('The loop has cycled {} time(s).'.format(x))  
        x += 1 # incriment the loop counter

    print('') # shifting a line back to the left one tab indicates
              # that the loop is over 

    # We can incriment by any value we like
    x = 2
    while x <= 10:
        print('The value in \'x\' is: {}'.format(x))
        print('The loop has cycled {:.0f} time(s)'.format(x / 2))
        x += 2
        
    print('')

def userLoop():
    """ While loops are usually used to cycle a block of code
     over and over until an abitrary endpoint is reached. The
     programmer does not need to be aware of when that ending
     condition will occur. This often occurs when we are waiting
     for specific user input."""
    print("\n{:*^70}".format("User Input Loop"))
    
    stringVar = ""
    while stringVar != "End":
        stringVar = input("Please enter a word. Type 'End' to exit the loop:")

def userBoolLoop():
    """ While loops can be combined with boolean comparisons to check
     several conditions at once"""
    print("\n{:*^70}".format("Loops with Bools"))

    stringVar = ""
    x = 0 
    while stringVar != "End" and x < 5:
        print("This loop will end in {} pass(es).".format(5 - x))
        stringVar = input("Please enter a word. Type 'End' to exit the loop:")
        x += 1

# Begin MAIN()
main()
