# Author: Mark Dencler
# Modified for python 3.7 by Charles Strovel 
# Description: This program shows how functions return values.

def main():
    """ Demonstrates how to use return values using the functions below """
    # By default, functions return the 'None' type.
    tempVar = nonReturner()
    print('The value returned by the function is: {}'.format(tempVar))

    # If a function returns a value, the call transforms into the return value.
    firstNumber = 5
    secondNumber = 7

    print('{} + {} = {}'.format(firstNumber, secondNumber, add(firstNumber, secondNumber)))
    print("")

    # A function can be designed to return multiple values
    # Note: When multiple return values are used, the order of the return values
    #       in the function should correspond with the order of the variables
    #       present in the lvalue when the call is made.
    sum, product = addAndMultiply(firstNumber, secondNumber)
    print('{} + {} = {}'.format(firstNumber, secondNumber, sum))
    print('{} * {} = {}'.format(firstNumber, secondNumber, product))
    print("")

    # Note: When returning two values, a function uses a data structure known as a 
    # tuple. A tuple is identical to a list, however it is imutable (can not be changed)
    otherAnswer = addAndMultiply(3, 5)
    print(otherAnswer)

    # otherAnswer[1] = 2 would cause an error! 


def nonReturner():
    print('This function is running, but doesn\'t explicitely return anything.')

def add(addend_1, addend_2):
    sum = addend_1 + addend_2
    return sum

def addAndMultiply(operand_1, operand_2):
    sum = operand_1 + operand_2
    product = operand_1 * operand_2
    return sum, product

# Begin MAIN()
main()
