#Author: Charles Strovel
#This program is designed to demonstrate mathmatical operations 
#multipule differnet ways of using Print() are shown, chose the correct
#method for the output you are attempting to display 

print("ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION")
# ADDITION
# The operator for addition is "+".
addendOne = 25
addendTwo = 13
sum = addendOne + addendTwo
print("%d + %d = %d" % (addendOne, addendTwo, sum))

# SUBTRACTION
# The operator for subtraction is "-".
subOne = 235
subTwo = 130 
difference = subOne - subTwo
print("{s0} - {s1} = {dif}".format(s0 = subOne, s1 = subTwo, dif = difference))

# MULTIPLICATION
# The operator for multiplication is "*".
mulOne = 8
mulTwo = 15
product = mulOne * mulTwo
print("{0:d} * {1:d} = {2:d}".format(mulOne, mulTwo, product))

# DIVISION 
# The operator for division is "/".
dividend = 119
devisor = 7
# note that this operation produces a float regardless of quotent and regardless 
# of dividend and devisor type 
quotent = dividend / devisor 
print(dividend, "/", devisor, "=",quotent)

print("\nEXPONENTS AND ROOTS")
# Exponents 
# The operator for exponents is "**". 
base = 3
power = 7
result =  base ** power
print("%d ** %d = %d" % (base, power, result))

# Roots
# The sqare root of n can also be expressed as n ** (1/2)
# Thus taking our result in the exponents example to the power
# of 1/power will give us back our base 
rootResult = result ** (1/power)
# note this will produce a float
print("Base: {0}\n{1} ** 1/{2} = {3}".format(base, result, power, rootResult))

print("\nMODULUS (Remainders)")
# MODULUS (remainders)
# The symbol for modulo is "%".
# This will return the remainder a division operation
dividend = 35
devisor = 8
remainder = dividend % devisor
# since % is used to escape characters for replacement, we need two % symbols to display
# modulo or % in strings 
print("%d %% %d = %d" % (dividend, devisor, remainder))

print("\nORDER OF OPERATIONS")
# ORDER OF OPERATIONS
# Mathmatical operations will be performed in the order of this list, top first
# From left to right in an equation 
# 1.) The contents of grouping brackets (), from inner most nested to outer most
# 2.) Exponents ** 
# 3.) Multiplcation, Division, Modulus
# 4.) Addition, Subtraction 
result = 2 + 4 * 7
print("The result is:", result)
result = 16 / 2 * 3
print("The result is:", result)
result = (5 + 4) ** 2 * 3
print("The result is:", result)
result = (5 - 7 ** 2) / -11
print("The result is:", result)
result = ((3 / 2) + 3) ** 2  
print("The result is:", result)

# TYPE PROMOTION (IMPLICIT CASTING)
print("\nTYPE CASTING AFTER MULTIPLICATION")
result = 4 * 5                      # int with int gives int
print("The result of int * int is:", result)
result = 4.0 * 5.0                  # float with float gives float
print("The result of float * float is:", result)
result = 4 * 5.0                    # float with int gives float
print("The result of int * float is:", result)
result = 25 / 5                     # division always produces a float 
print("The result of int / int is: ", result)
input()