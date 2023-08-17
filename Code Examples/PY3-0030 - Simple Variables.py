# Author: Mark Dencler
# Edited for 3.7 By Charles Srovel 
# Description: This program demonstrates variable types and simple usage.

#if you want to make a variable in Python, just pick a name and assign a value
someNumber = 4

# an integer variable type is automatically declared and assigned the value 4
print("\nthe number is now")
print(someNumber)

# we can give the variable a new value by simply assigning it
someNumber = 5
print("\nthe number is now")
print(someNumber)

# There are three main types of variables in Python (int, float, and string).
# We do not explicitly declare a variable's type.  Instead, the type is
# inferred based on its usage.

# When we assign a floating-point value to 'someNumber' it becomes a float.
someNumber = 4.5
print("\nthe number is now")
print(someNumber)

# In the same way, we can convert number number to a string.
someNumber = 'not a number at all'
print("\nthe number is now")
print(someNumber)

# When a line of code modified the type of a variable, a new variable is created
# on the call stack and the variable's name is reassigned to reference the new
# value.  The old value is still on the call stack but unaccessible.
input('\nPress Any Key To Continue')