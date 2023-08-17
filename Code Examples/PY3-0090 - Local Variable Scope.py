# Author: Mark Dencler
# Edited for 3.7 by Charles Strovel 
# Description: This program demonstrates the concept of local variable scope.

def main():
    # When a variable is declared in a function, it automatically assumes
    # local scope.  The variable exists and can only be accessed in the
    # function in which it was declared.
    variable = 5
    otherVariable = 10

    # in main(), variable has a value of 5
    print('The value in variable is:', variable)

    # in main(), otherVariable has a value of 10
    print('The value in otherVariable is:', otherVariable)

    # main() calls a different function 
    someFunction()

    #even though main() has called someFunction(), main() does not have the scope
    #to access someFunctionVariable
    #print('The value in someFunction Variable is:', someFunctionVariable) #ERROR!
    input()
    
def someFunction():
    # When you are in a function, you can declare another variable with
    # the same name, but it is a different variable because they have
    # different scopes.
    variable = 10
    someFunctionVariable = 22

    # variable in main() contains a value of 5, where as the same named variable
    #in this function contains a value of ten 
    print('The value in variable is:', variable)
    #of course, some function can have variables that are not named in main() as well 
    print('The value in someFunctionVariable is:',someFunctionVariable)

    # we cannot access otherVariable because it does not have scope
    # in someFunction()
    #print('The value in otherVariable is:', otherVariable)  #ERROR!

# BEGIN MAIN()
main()
