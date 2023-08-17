# Author: Charles Strovel 
# Description: This program demonstrates the use of external modules.

def externalFunctionOne():
    """ Simple statement to demonstrate module imports """
    print('This statement is being displayed in an external module')

def externalFunctionTwo():
    """ Simple statement to demonstrate module imports """
    print('Remember, to gain access to the functions in another file,')
    print('you must provide the proper import statement at the top of')
    print('the code file that will use the external functions.')

def externalFunctionThree(num1, num2):
    """ Multiplies two numbers together """ 
    return num1 * num2

def externalFunctionFour(thing1, thing2):
    """ creates a sentance with passed data """
    print("This module has included your data, '{}' and '{}' in this sentance.".format(thing1,thing2))