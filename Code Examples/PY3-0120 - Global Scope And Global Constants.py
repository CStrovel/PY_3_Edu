# Author: Mark Dencler
# Description: This program demonstrates the concept of global scope and the
# proper way to simulate the behavior of global constants.

# When a variable is declared outside of a function, it assumes global
# scope.  The variable can be accessed anywhere in the program, but can
# only be modified outside of a function and in functions where the variable
# has been explicitely declared as global.

# GLOBAL VARIABLES
GlobalVariable = 45         # global variables should not be in all caps 
GLOBAL_CONSTANT_PI = 3.14   # global constants should be named with all caps

# inside of main(), we can access both global variables, but we
# can only modify a value that is explicitely declared as global
def main():
    # this statement grants write access to the global variable in main()
    global GlobalVariable

    # display the values in the variables
    print('The value in GlobalVariable is:', GlobalVariable)
    print('The value in GLOBAL_CONSTANT_PI is:', GLOBAL_CONSTANT_PI)
    # Take note that GLOBAL_CONSTANT_PI was referenced in the previous
    # statement.  It is a global, but has not been explicitely declared,
    # so its name is known, but only write access is allowed.  In other
    # words, it has been registered as a global.

    # change the values in the globals
    GlobalVariable = 50
    #GLOBAL_CONSTANT_PI = 2.1817     # ERROR
    # The previous line will fail because GLOBAL_CONSTANT_PI was already
    # accessed and cataloged as a global.  This means it is read-only.

    # display the values after the modifications
    print('The value in GlobalVariable is:', GlobalVariable)
    print('The value in GLOBAL_CONSTANT_PI is:', GLOBAL_CONSTANT_PI)

    # call otherFunction()
    otherFunction()
    
    # input to pause display
    input()




def otherFunction():
    # when we declare a local-scope variable with the same name as an
    # already existing global, the local-scope variable supercedes the
    # global
    GlobalVariable = 100     # not really a global variable
    print('The value in GlobalVariable is:', GlobalVariable)
    # Take note that this example differs from the example with
    # GLOBAL_CONSTANT_PI earlier in main.  In this function, the
    # variable GlobalVariable is used in an assignment.  The name
    # has not been used before that point though, so a new variable
    # with the same name, GlobalVariable, was created and has function
    # scope only.  This version is different from the global variable
    # called GlobalVariable as well and the names are resolved with
    # the Python scope rules.
    
    # inside of the function, we can access GLOBAL_CONSTANT_PI just
    # as we could in main()
    print('The value in GLOBAL_CONSTANT_PI is:', GLOBAL_CONSTANT_PI)

    
# BEGIN MAIN()
main()
