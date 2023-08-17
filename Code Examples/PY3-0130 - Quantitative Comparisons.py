# Author: Charles Strovel
# Description: this program demonstrates comparison operators.

def main():
    # Comparison operators allow us to compare the values of two numbers
    # Python supports the same operators used by C/C++
    # Less Than: <
    # Less Than or Equal To: <=
    # Greater Than: >
    # Greater Than or Equal To: >=
    # Equal To: ==
    # Not Equal To: !=
    # These operators will result in a boolean value, that is, a
    # Value that is either True or false 

    # Less Than: < 
    # The less than comparison operator evaluates if the value on the
    # left side is less than the value on the right side. In this case,
    # if x is less than y.
    print("Less Than Comparisons:")
    x = 6
    y = -4
    result = x < y #comparison 
    print("The result of ",x , '<', y, " is ", result)
    x = 5
    y = 25
    result = x < y #comparison 
    print("The result of ",x , '<', y, " is ", result)

    # Less Than or Equal To: <=
    # The less than or equal to operator works the same way as the
    # less than operator, however, it will return true if the numbers
    # are equivalant. 
    print("\nLess Than or Equal to Comparisons:")
    x = 22
    y = 24

    result = x <= y
    print("The result of ",x , '<=', y, " is ", result)

    result = y <= x
    print("The result of ",y , '<=', x, " is ", result)

    x = y # but what if x is the same as y?
    result = x <= y
    print("The result of ",x , '<=', y, " is ", result)

    # Greater Than: >
    # The Greater Than comparison operator evaluates if the value on the
    # left side is less than the value on the right side. In this case,
    # if x is greater than y.
    print("\nGreater Than Comparisons:")
    x = 18
    y = -1
    result = x > y
    print("The result of ",x , '>', y, " is ", result)
    result = y > x
    print("The result of ",y , '>', x, " is ", result)

    # Greater Than or Equal To: >=
    # The Greater Than or Equal To comparison operator works the
    # same way as the greater than operator, however will also
    # return true if the two values are equal.
    print("\nGreater Than or Equal to Comparisons:")
    x = 3
    y = -40
    result = x >= y
    print("The result of ",x , '>=', y, " is ", result)
    result = y >= x
    print("The result of ",y , '>=', x, " is ", result)

    x = y # but what if x is the same as y?
    result = x >= y
    print("The result of ",x , '>=', y, " is ", result)

    # Equal To: ==
    # Because the = is already used as the assignment operator
    # to evaluate if two numbers are equal to each other, we must use
    # == insted.
    print("\nEqual To:")
    x = 3
    y = 5
    result = x == y
    print("The result of ",x , '==', y, " is ", result)
    x = y # but what if x is the same as y?
    result = x == y
    print("The result of ",x , '==', y, " is ", result)

    # Not Equal To: !=
    # Not Equal To evaluates to false when values 
    # are equal to each other, and true when the values 
    # are not equal to each other.
    print("\nNot Equal To:")
    x = 23
    y = 48
    result = x != y
    print("The result of ",x , '!=', y, " is ", result)
    x = y # but what if x is the same as y?
    result = x != y
    print("The result of ",x , '!=', y, " is ", result)

    #input to keep output on screen
    input()
    

# Begin MAIN()
main()
    
