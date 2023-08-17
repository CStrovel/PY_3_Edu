# Author: Charles Strovel
# Description: This program demonstrates positional passing of arguments between functions
# by re-running the same mathmatical function with different argument positions

# demo mathmatical function
# Poisitional argument passing reffers to the order, left to right, in which
# arguments are passed when the function is called. When demoMathFunction() below 
# is invoked: demoMathFunction(var1, var2, var3, var4), the value in var 1 is assigned
# to the variable numOne, the value in var2 is assigned to the variable numTwo, and so on
def demoMathFunction(numOne, numTwo, numThree, numFour):
    # do some math
    product = numOne + (numTwo - numThree) * numFour

    # show the output and result of the math
    print("{0} + ({1} - {2}) * {3} = {4}".format(numOne, numTwo, numThree, numFour, product))

# Declare main function
def main():
    # first lets get some numbers from the user
    var1 = eval(input('Please input your first number :'))
    var2 = eval(input('Please input your second number :'))
    var3 = eval(input('Please input your third number :'))
    var4 = eval(input('Please input your fourth number :'))

    # now lets call our demoMathFunction(). For this invocation the value of var1 is 
    # assigned to numOne in demoMathFunction(), var2 is assigned to numTwo, var3 is
    # assigned to numThree, and var4 is assigned to numFour
    demoMathFunction(var1, var2, var3, var4)

    # for this invocation, var2 will become numOne, var3 will become numTwo, var4
    # will become numThree, and var1 will become numFour
    demoMathFunction(var2, var3, var4, var1)

    # this invocation will assign var4 to numOne, var2 to numTwo, var1 to numThree, and
    # var3 to numFour
    demoMathFunction(var4, var2, var1, var3)

    #input to pause the screen
    input()
    
#call main()
main()