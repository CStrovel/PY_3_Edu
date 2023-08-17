# author Charles Strovel
# This program demonstrates shorthand mathmatical operators.

# It may be useful to add, subtract, multiply or divide a variable
# by a number, and then imediatly reassign the resulting vlaue
# to the origional variable.

# we can manually do the reassignment, in the form of varX = varX + 1,
# or we can use short hand operators that take the form of +=, -=, *=,
# /= and %= 

# This is especially useful in loops, as shown in the next example.

def main():
    # Scroll down to view function definitions for examples 
    shortHandSum()
    shortHandDifference()
    shortHandMultiplication()
    shortHandDivision()
    shortHandMod()
    input()

def shortHandSum():
    """This function provides examples for short
    hand addition operation usage."""
    print("{:*^70}".format("Addition"))
    x = 5           # set the value to 5
    print('x has a value of: {}'.format(x))
    x = x + 5       # normal sum assignment
    print('x = x + 5 results in x becoming: {}'.format(x))
    x += 5         # shorthand sum assignment. Peforms
                   # the same operation as the one above 
    print('x += 5 results in x becoming: {}'.format(x))

    # x += 1 can be used to easily incriment for a while loop
    # or other counter
    x += 1
    print('x += 1 results in x becoming: {}'.format(x))
    x += 1
    print('x += 1 results in x becoming: {}'.format(x))
    x += 1
    print('x += 1 results in x becoming: {}'.format(x))

def shortHandDifference():
    """This function provides examples for short
    hand subtraction."""
    print("\n{:*^70}".format("Subtraction"))
    x = 50       # set the value to 5
    print('x has a value of: {}'.format(x))
    x = x - 5       # normal difference assignment
    print('x = x - 5 results in x becoming: {}'.format(x))
    x -= 5         # shorthand difference assignment. Peforms
                   # the same operation as the one above 
    print('x -= 5 results in x becoming: {}'.format(x))

    # x -= 1 can be used to easily decriment for a while loop
    # or other counter
    x -= 1
    print('x -= 1 results in x becoming: {}'.format(x))
    x -= 1
    print('x -= 1 results in x becoming: {}'.format(x))
    x -= 1
    print('x -= 1 results in x becoming: {}'.format(x))

def shortHandMultiplication():
    """This function provides an example for short
    hand multiplication."""
    print("\n{:*^70}".format("Multiplicaiton"))
    x = 5      # set the value to 5
    print('x has a value of: {}'.format(x))
    x = x * 2       # normal product assignment
    print('x = x * 2 results in x becoming: {}'.format(x))
    x *= 2         # shorthand product assignment. Peforms
                   # the same operation as the one above 
    print('x *= 2 results in x becoming: {}'.format(x))

def shortHandDivision():
    """This function provides an example for short
    hand division."""
    print("\n{:*^70}".format("Division"))
    x = 100     # set the value to 100
    print('x has a value of: {}'.format(x))
    x = x / 5       # normal quotent assignment
    # note that this operation changes x into a float
    print('x = x / 5 results in x becoming: {}'.format(x))
    x /= 2         # shorthand quotent assignment. Peforms
                   # the same operation as the one above 
    print('x /= 2 results in x becoming: {}'.format(x))

    # integer division uses the same shorthand with an extra slash
    x = 100
    print('x has a value of: {}'.format(x))
    x //= 34
    print('x //= 34 results in x becoming: {}'.format(x))

def shortHandMod():
    """This function provides an example for short
    hand modulo."""
    print("\n{:*^70}".format("Mod"))
    x = 100     # set the value to 100
    print('x has a value of: {}'.format(x))
    x = x % 27       # normal mod assignment
    print('x = x % 27 results in x becoming: {}'.format(x))

    x = 100     # resetting x to 100
    print('x has a value of: {}'.format(x))
    x %= 27       # shorthand mod assignment. Peforms
                   # the same operation as the one above 
    print('x %= 27 results in x becoming: {}'.format(x))


# call main
main()
    
    
    
    
    
    

