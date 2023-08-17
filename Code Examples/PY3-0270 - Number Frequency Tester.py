# Author: Mark Dencler
# Modified for Python 3.7 by Charles Strovel 
# Description: This program generates an arbitrary series of random integers
#    and keeps a frequency count of the the logical ranges in which the
#    numbers occur.  These frequences are then displayed on the screen
#    to show is the distribution of values generated is indeed uniform.
#    The student's program should contain additional code that tests
#    the uniformity of the values returned by the floating-point pseudo
#    random number generation utilities as well.

#Import the random module 
import random

# global variable that contains the number of random integers to generate 
NUMBERS_TO_GENERATE = 10000

def main():
    """ sums the occurance of numbers betwen 1 and 100, tallying by a range of 10 """ 
    # create counter variables that will hold the frequences of numbers
    # that fall within certain ranges
    g_01 = 0    # 00 - 09
    g_02 = 0    # 10 - 19
    g_03 = 0    # 20 - 29
    g_04 = 0    # 30 - 39
    g_05 = 0    # 40 - 49
    g_06 = 0    # 50 - 59
    g_07 = 0    # 60 - 69
    g_08 = 0    # 70 - 79
    g_09 = 0    # 80 - 89
    g_10 = 0    # 90 - 99
    g_ERR = 0   # counts any numbers that are not in range

    # generate a random number and bump the appropriate counter
    for _ in range(NUMBERS_TO_GENERATE):
        rNumber = random.randrange(0, 100)
        if rNumber >= 0 and rNumber <= 9:
            g_01 += 1
        elif rNumber >= 10 and rNumber <= 19:
            g_02 += 1
        elif rNumber >= 20 and rNumber <= 29:
            g_03 += 1
        elif rNumber >= 30 and rNumber <= 39:
            g_04 += 1
        elif rNumber >= 40 and rNumber <= 49:
            g_05 += 1
        elif rNumber >= 50 and rNumber <= 59:
            g_06 += 1
        elif rNumber >= 60 and rNumber <= 69:
            g_07 += 1
        elif rNumber >= 70 and rNumber <= 79:
            g_08 += 1
        elif rNumber >= 80 and rNumber <= 89:
            g_09 += 1
        elif rNumber >= 90 and rNumber <= 99:
            g_10 += 1
        else:
            g_ERR += 1 

    # display a table showing the status of the counter
    print('GROUP #01 (00 - 09) FREQUENCY: {}'.format(g_01))
    print('GROUP #02 (10 - 19) FREQUENCY: {}'.format(g_02))
    print('GROUP #03 (20 - 29) FREQUENCY: {}'.format(g_03))
    print('GROUP #04 (30 - 39) FREQUENCY: {}'.format(g_04))
    print('GROUP #05 (40 - 49) FREQUENCY: {}'.format(g_05))
    print('GROUP #06 (50 - 59) FREQUENCY: {}'.format(g_06))
    print('GROUP #07 (60 - 69) FREQUENCY: {}'.format(g_07))
    print('GROUP #08 (70 - 79) FREQUENCY: {}'.format(g_08))
    print('GROUP #09 (80 - 89) FREQUENCY: {}'.format(g_09))
    print('GROUP #10 (90 - 99) FREQUENCY: {}'.format(g_10))
    print('GROUP #ERR          FREQUENCY: {}'.format(g_ERR))

# Begin MAIN()
main()
