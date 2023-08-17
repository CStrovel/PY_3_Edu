# Author: Charles Strovel
# This program demonstrates function structure and function invocation

#FUNCTION BASICS 
# Functions are structures or "blocks" of code that can be executed by invoking 
# their name. This allows us to use the same block of code several times and from
# different places within a program. Functions can recieve data through paramiter passing
# and return data as well

# Before a function can be used it must be defined. This is accomplished
# by using the def statement, followed by a function name, followed by
# the function parameters, and finally a colon  
def exampleFunction(param1, param2):
    # python does not use brackets {} to define a function's body, instead
    # python uses indentation to indicate which instructions belong to a function
    print("")
    #this function prints the value of the two arguments it is passed
    print(param1)
    print(param2)

    # every line following that is indented at least once is considered inside of the function
    # body. As soon as a line has no indentation it closes out the function body.

# statements can be used inside or outside of functions, but functions can be used for
# reusability and readability
print("this line is outside of exampleFunctions body, as it is fully left justified."\
    "This also denotes the close of exampleFunction")

# functions can be passed arguments (aka parameters) to use within the body of the function 
# lets set up two example strings to pass to our function
str1 = "This is be printed from inside exampleFunction"
str2 = "This is also be printed from inside exampleFunction"

# functions can be invoked (called/used/etc) by stating the functions name followed by passing 
# it's expected arguments (things inside these brackets). There will be more on function passing
# later
exampleFunction(str1,str2)

# in other words, function invocation looks like "functionName(parameter1,paramiter2,...)"

# functions can call other functions, infact, that is what we are doing whenever we call
# print()! 

input()