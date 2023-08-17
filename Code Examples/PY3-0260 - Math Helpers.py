# Author: Mark Dencler
# Modified for Python 3.7 by Charles Strovel
# Description: This program illustrates the math helper resources available
#              in Python's math library module.

# import the math module 
import math

def main():
    # Mathematical constants 'pi' and 'e'.
    print('The constant value pi is: {}'.format(math.pi))
    print('The constant value e is : {}'.format(math.e))
    print('')

    # FLOOR() and CEIL() - Mathematical functions that allow you to take
    #   a floating point value and move it to the next integer on the
    #   number line (ceiling) or the previous integer on the number line.
    number = 3.67
    print('The value in the variable is: {}'.format(number))
    print('The floor of that value is: {}'.format(math.floor(number)))
    print('The ceiling of that value is: {}'.format(math.ceil(number)))
    print('')

    # SQRT() - Returns the square root of a number as a floating-point.
    number = 81
    print('The value in the variable is: {}'.format(number))
    print('The square root of that value is: {}'.format(math.sqrt(number)))
    print('')

    # LOG(), LOG10(), and EXP() - Mathematical functions that allow
    #    basic operations related to logorithms and exponentiation to
    #    be performed.
    number = 100.0
    print('The value in the variable is: {}'.format(number))
    number = math.log10(number)
    print('The base-10 logarithm of the value is: {}'.format(number))
    number = math.log(number)
    print('The natural logorithm of that value is: {}'.format(number))
    print('The natural exponentiation of that value is: {}'.format(math.exp(number)))
    print('')

    # SIN(), COS(), TAN(), DEGREES(), RADIANS() - Mathematical functions
    #    that allow you to perform basic trigonometric operations in Python.

    # We can convert from degrees to radians with RADIANS().
    degrees = 45
    radians = math.radians(degrees)
    print('{} degrees is the same as {} radians.'.format(degrees, radians))

    # We can take the sine, cosine, and tangent of values that are presented
    # in radians.
    print('sin({}) = {}.'.format(radians, math.sin(radians)))
    print('cos({}) = {}.'.format(radians, math.cos(radians)))
    print('tan({}) = {}.'.format(radians, math.tan(radians)))
    print('')

    # We can convers from radians to degrees with DEGREES()
    degrees = math.degrees(radians)
    print('{} radians is the same as {:.0f} degrees.'.format(radians, degrees))
    

# Begin MAIN()
main()
