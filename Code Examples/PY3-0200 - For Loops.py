# Author: Charles Strovel
# Description: Demonstrates basic use of python for loops

def main():
    """ Provides flow control for loop examples """

    # For loops in python rely on an "iterator", any data type that 
    # can be counted through sequentially. the function loopsWithRange() shows examples
    # of how to loop based on integer values.
    loopsWithRange()

    # examples of iterating through other data types
    print("")
    loopsWithLists()

def loopsWithRange():
    """ Function demonstrates for loop basics using range()"""
    # Range is a specialized python function that gives us an iterator
    # with a length equivalant to the integer pased to it. This means that
    # range(10) will produce an iterator with 10 indexes, from 0 through 9

    # The loop variable can be used as an incrimenter for running through a
    # list or changing the behavior of an equation
    print("for x in range(10):")
    for x in range(10):
        print("x = {:3}. x * 5 = {}".format(x, x * 5))

    # Range can be used with two parameters. The first one provides a lower
    # bounds for the resulting iterator's index, and the second one provides
    # an upper bounds.
    print("\nfor x in range(3,12):")
    for x in range(3, 12):
        print("x = {:3}. x * 5 = {}".format(x, x * 5))

    # Range can be used with three parameters. The first two providing a lower
    # and upper bound. The third controls the iterators step. 
    print("\nfor x in range(10, 30, 2):")
    for x in range(10, 30, 2):
        print("x = {:3}. x * 5 = {}".format(x, x * 5))

    # The third parameter of range can be used to count backwards by assigning it a
    # negative number.
    print("\nfor x in range(10, 0, -1):")
    for x in range(10, 0, -1):
        print("x = {:3}. x * 5 = {}".format(x, x * 5))
    
def loopsWithLists():
    """ Function demonstrates for loops using a list as the iterator """

    # For loops can be controled by a list. For each run through the loop, the loops
    # control variable will be assigned the list value at the current index
    for x in [1, 2, 3, 4, 5]:
        print("The current value of 'x' is: {}".format(x))

    # Iteration can be done with lists that are not just intgers
    print("")
    for x in [2.25, 3.14, 6.6, 12.111111, 36]:
          print("The current value of 'x' is: {}".format(x))

    # Strings can also be used for iteration
    print("")
    for x in "This is a string":
        print("The current value of 'x' is:{}".format(x))

    # We can also combine the two ideas to iterate through strings aranged in a list
    print("")
    counter = 1
    # outer loop iterates through each word
    for word in ["This", "is", "a" , "string"]:
        print("The letters in word {} are: ".format(counter), end = "")
        
        # Inner loop iterates through each letter in the current word 
        for letter in word:
            print( " " + letter + ",", end = "")
        
        # clean up and loop management. Counter is only needed to display which
        # word we are currently in
        print("")
        counter += 1

main() 

    
          
