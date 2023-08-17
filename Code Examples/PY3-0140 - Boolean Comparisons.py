# Author: Charles Strovel 
# Description: The program demonstrates the boolean logic operators.

def main():
    # In Python, there is support for boolean comparisons. Compairing two
    # boolean true or false values. 
    # Logical And - and 
    # Logical OR - or
    # Logical NOT - not

    # new variable type "boolean". Booleans can store a 
    # True or a False as their value. 
    x = True           
    y = False
    # (note: C/C++ programmers... Do not stick numbers into boolean
    #  variables.  Zero is not False and non-zero is not True)
    
    # AND comparisons
    # This logical comparison operator evaluates if both sides of the
    # operator are true. If either boolean value is false, and will evaluate
    # to false as well
    print("{:*^70}".format("Logical 'AND' comparisons"))
    print("If both operands are true, the 'and' evaluates to true ")
    result = x and x  
    DisplayResult(x, x, "and", result)
    print("\nIf at least one operand is false, and evaluate to false")
    result = x and y
    DisplayResult(x, y, "and", result)
    result = y and x
    DisplayResult(y, x, "and", result)
    result = y and y 
    DisplayResult(y, y, "and", result)

    # OR comparisons
    # Or comparison operators evaluate if  the value to 
    # either side of the operator is true. If either boolean value is 
    # true, or will evaluate to true
    print("\n{:*^70}".format("Logical 'OR' comparisons"))
    print("If at least one operand is true, the 'or' evaluates to true as well")
    result = x and x  
    DisplayResult(x, x, "or", result)
    result = x and y
    DisplayResult(x, y, "or", result)
    result = y and x
    DisplayResult(y, x, "or", result)
    result = y and y 
    print("If both sides are false, the 'or' evaluates to false as well")
    DisplayResult(y, y, "or", result)

    # NOT comparison operator 
    # not comparison operators evaluate if their operand is
    # true or false. If the operand is true, not evaluates to
    # false. If the operand is false, not evaluates to true.
    print("\n{:*^70}".format("Logical 'NOT' operations"))
    result =  not x
    DisplayResult("", x, "not", result)
    result =  not y
    DisplayResult("", y, "not", result)

    input()

# Use a function to avoid having to repeat code  
def DisplayResult(x, y, operator, result):
    print(x, operator, y , "=", result)

# Begin MAIN()
main()
