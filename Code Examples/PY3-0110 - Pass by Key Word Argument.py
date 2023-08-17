# Author: Charles Strovel
# Description: This program demonstrates key word argument passing (kwargs) using
# a demo mathmatical function 

# demo mathmatical function
# key word arguments, or kwargs allow the programmer to directly refference parameter 
# names when invoking a function to directly assign values. 
# demoMathFunction(numThree = var1, numFour = var2,...)
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

    # now lets call our demoMathFunction(). This time however we will change the kwargs
    # and not the position that the variables are passed in
    demoMathFunction(numOne = var1, numTwo = var2, numThree = var3, numFour = var4)

    # now lets change up the the kwargs being used
    demoMathFunction(numThree = var1, numFour = var2, numOne = var3, numTwo = var4)
    demoMathFunction(numFour = var1, numTwo = var2, numOne = var3, numThree = var4)

    # kwargs can even be combined with positional passing, though all positional arguments
    # must be on the left hand side of the argument list
    demoMathFunction(var1, var2, numFour = var3, numThree = var4)
     #demoMathFunction(numFour = var1, numThree = var2, var3, var4) #ERROR!

    #input to pause the screen
    input()
    
#call main()
main()