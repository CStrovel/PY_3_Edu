# Author: Charles Strovel
# Description: Program demonstrates how to cast variables as different types 

# While variables in python are weakly typed, that is they will take on the type of 
# whatever value is assigned to them, some mathmatical operations or functions may
# be expecting a specific data type.

# More importantly, relying on eval() to convert our inputs to whatever datatype the user
# inputs is insecure. eval() executes the passed paramiter as a python statement. This means
# a string passed to eval() can be used to execute code! From this point on, type casting and
# input validation should be used instead of eval.  
def main():
    """ Demonstrates type casting

    This program shows how to type cast, as well as well as the effect of 
    converting one data type to another """ 

    # CASTING INTS
    # set the values
    var_1 = int(3)
    var_2 = int(15.3)
    var_3 = int(float("23.6"))
    var_4 = int(True)
    var_5 = int(False)
    
    # display the values
    DisplayValues(var_1, var_2, var_3, var_4, var_5)

    # don't attempt to cast a string as an int
    #var = int('This will not work.')
    #DisplayValue(var)
    print('')

    # CASTING FLOATS
    # set the values
    var_1 = float(3)
    var_2 = float(15.3)
    var_3 = float("23.6")
    var_4 = float(True)
    var_5 = float(False)

    # display the values
    DisplayValues(var_1, var_2, var_3, var_4, var_5)
    print('')

    # don't attempt to cast a string that does not contain only numeric characters to
    # a float or int, this will cause an error. 
    # var_1 = float("This has no numbers in it") will result in an error! 

    # Like wise, you can not convert a string that contains data that would be a valid floating 
    # point value directly to an integer. int("2.55") will not work. You must first convert it
    # to a float, than to an int! 
    var_1 = int(float("2.55"))
    DisplayValue(var_1)
    print('')

    # CASTING BOOLEANS
    # set the values
    var_1 = bool(3)
    var_2 = bool(15.3)
    var_3 = bool("23.6")
    var_4 = bool(True)
    var_5 = bool(False)

    # display the values
    DisplayValues(var_1, var_2, var_3, var_4, var_5)

    # a string can be cast as a boolean... non-empty string return
    #    the value True and empty string return the value False
    var = bool('This will not work.')
    DisplayValue(var)
    var = bool('')
    DisplayValue(var)
    print('')

    # CASTING STRINGS
    var_1 = str(3)
    var_2 = str(15.3)
    var_3 = str("23.6")
    var_4 = str(True)
    var_5 = str(False)

    # display the values
    DisplayValues(var_1, var_2, var_3, var_4, var_5)

    
# display the values in a single variable
def DisplayValue(var_1):
    print('The variable contains: {}'.format(var_1))

# displays the values in multiple varaibles
def DisplayValues(var_1, var_2, var_3, var_4, var_5):
    print('The 1st variable contains: {}'.format(var_1))
    print('The 2nd variable contains: {}'.format(var_2))
    print('The 3rd variable contains: {}'.format(var_3))
    print('The 4th variable contains: {}'.format(var_4))
    print('The 5th variable contains: {}'.format(var_5))

# Begin MAIN()
main()
