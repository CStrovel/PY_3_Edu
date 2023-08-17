# Author: Mark Dencler
# modified for python 3.7 by Charles Strovel 
# Description: This program demonstrates the generation of random numbers
#              using the Python random utilities.

# Import the random number module 
import random

# randint(), randrange(), random(), uniform()

def main():
    # The random number generator automatically seeds to the time
    # in the system clock. However, we can override the default
    # seed value by calling random.seed().
    #random.seed(38584)

    # The seed value can be forced to move far away from its current
    # state by using random.jumpahead().  This function would be useful
    # in programs where multiple random number generators are being used
    # for a variety of tasks and the user needs the output from each
    # generator to be substantially different from the others.
    #random.jumpahead(48394)   # the value is used to calculate an offset

    # random.randint() - This function is used to generate random numbers that
    #             fall within the range designated by the arguments.
    print('Generating 5 random numbers between 1 and 100.')
    for _ in range(5):
        number = random.randint(1, 100)
        print(number)
    print('')

    # random.randrange() - This function generates random numbers in the same
    #               fashion that the range() function is used to generate
    #               lists used for loop control.  The same three overloaded
    #               implementations for range() also apply to randrange().
    print('Generating 10 random numbers between 0 and 5.')
    for _ in range(10):
        number = random.randrange(6)
        print(number)
    print('')

    print('Generating 10 random numbers between 10 and 15.')
    for _ in range(10):
        number = random.randrange(10, 16)
        print(number)
    print('')

    print('Generating 10 random, even numbers between 100 and 150.')
    for _ in range(10):
        number = random.randrange(100, 151, 2)
        print(number)
    print('')

    # random.random() - This function generates a random floating-point number
    #            on the interval [0, 1.0).
    print('Generating 10 random numbers on [0.0, 1.0).')
    for _ in range(10):
        number = random.random()
        print(number)
    print('')

    # UNIFORM() - This function generates a random floating-point number
    #             that sits between the two provided argument values.
    print('Generating 10 random numbers on [2.5, 3.7].')
    for _ in range(10):
        number = random.uniform(2.5, 3.7)
        print(number)
    print('')

    # Note: The numbers can be reversed, which will change the behavior
    #       of the uniform().
    print('Generating 10 random numbers on [2.5, 3.7].')
    for _ in range(10):
        number = random.uniform(3.7, 2.5)
        print(number)
    print('')

# Begin MAIN()
main()
