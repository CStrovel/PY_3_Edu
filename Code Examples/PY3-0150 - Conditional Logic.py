# Author: Charles Strovel
# Description: This program demonstrates conditional logic structures.

# Python supports three different conditional logic sructures
# The 'if' statement executes a block of code if a given statement is true

# The 'else' statement is used in conjunction with the 'if' statement to
# execute a block of code when the 'if' has recieved a false statement

# The 'elif' statement is used evaluate a second, third, fourth...etc
# expression after an if statement, using an 'else' to close the block of statements
def main():
    # declaring variables
    x = -1
    y = 7
    
    # if/elif can also evaluate boolean statements 
    firstBool = True;
    secondBool = False;  

    # IF conditional logic statements 
    print("{0:*^75}".format("'if' Conditional Logic"))
    # 'if' statements execute the associate code block when the
    # quantative comparison or boolean it is evaluating is true 
    # are true 
    # 'if' x is less than y, execute the block indented beneath it
    if x < y:
        print(" Code Block 1:")
        print("if x < y: evaluated to true")
        print(" So the 'if' statement executed the first code block\n")

    # 'if' x is greater than y, execute the block indented beneath it
    if x > y:
        print(" Code Block 2:")
        print("if x > y: evaluated to true")
        print( "So the if statement executed the second code block\n")

    # 'if' statements can also evaluate boolean values
    if firstBool:
        print("FirstBool is true, so this code is executed\n")

    if secondBool:
        print("SecondBool is false, so this will never execute without modifying the program\n")

    # ELSE conditional logic
    # 'else' conditional logic statements are used with 'if' statements
    # to execute the code block at the end of an if/elif chain. 
    # this code only executes when all other statements have proven false 
    print("{0:*^75}".format("'else' Conditional Logic"))
    if x < y:
        print("the 'if' statement executed, so the associated 'else' will not")
    else:
        print("This will not execute as the if statement above it has already executed")
            
    print("")
    if secondBool:
        print("This will not execute, as the boolean value is false\n")
    else:
        print("The 'if' statement above this 'else' recieved a false condition,\n so this code is executed instead\n")

    # ELSE-IF conditional logic
    # 'elif' conditional statements are used to evaluate an arbitrary number of expressions
    # begin with an 'if' statement, then an 'elif' for each other condition you want to test
    # end the line of 'if' 'elif' statements with an else

    # only one of these 'if'/'elif' statements is true, which one is it? 
    print("{0:*^75}".format("'elif' Conditional Logic"))
    if x > y:
        print("This code executes if x is greater than y")
    elif x > 25:
        print("This code executes if x is greater than 25")
    elif firstBool:
        print("This code executes if firstBool is true")
    elif secondBool:
        print("This code executes if secondBool is true")
    else:
        print("this code executes if no other statements above are valid.")

    print("")
    # 'if' 'elif' logic terminates at the first true condition
    # both of these conditions are true, but only the 'if' executes 
    if x < y:
       print("{} is less than {}".format(x, y))
    elif firstBool:
       print("firstBool is true")

    #input to pause the screen
    input()
    
#main function call
main()
