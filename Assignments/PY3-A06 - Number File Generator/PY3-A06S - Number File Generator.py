# Author: Charles Strovel
# Description: This program is sample code for weekly assignment 6,
# random number generator 

# Imports
import random

# Global Variables
FILE = "A06S-DataFile.dat"                  # The name of the file this program writes to
LOWER_BOUND = 0                             # Lower boundary for random number value 
UPPER_BOUND = 10000                         # Upper boundary for random number value
NUM_ELEMENTS = random.randint(0,5000)       # Prove program handles arbitrary file lengths 

def main():
    # generate the random number file
    generateRandomNumberFile(NUM_ELEMENTS)

    # find the average value of all numbers in file
    elementCount, averageValue = determineAverageValue(FILE)

    # display results
    displayCalculations(elementCount, averageValue)

def generateRandomNumberFile(numberOfElements):
    """Generates a file with an abitrary ammount of random number entries

    This function will demonstrate python file output using a with statement"""

    # use of 'with' to automatically close file when writes are finished
    # also allow clear code block deleniation 
    with open(FILE, 'w') as file:

        # loop through each element
        for i in range(numberOfElements):
            # write random number delimited by \n 
            file.write("{}{}".format(random.randrange(LOWER_BOUND, UPPER_BOUND + 1),'\n'))
        
        


def determineAverageValue(fileName):
    """Counts and averages some abitarary data

    Reads input file for numerical data. Tallys numeric entries and takes an average.
    Discards non numeric data and indicates the problem to the user without crashing. This
    function will demonstrate traditional file input.
    """

    # varables
    tally = 0
    average = 0
    total = 0 
    file = open(fileName, 'r')

    # Iterate over the file object
    for line in file:
        # Attempt to add the current line of the file to the total
        try:
            total += float(line)     # read in line and convert it to float 

        # If adding the line fails due to non numeric data
        except:
            tally -= 1          # do not count this line in the total 
            print("Non numeric data {} found. Discarding line.".format(line))

        # incriment the tally. this is canceled out if the attempted arithmatic is excepted 
        tally += 1

    # we are finished with the file, so we can close it
    file.close()

    # take the average only if tally != 0
    if tally != 0:
        average = total / tally
  
    return tally, average 

def displayCalculations(tally, average):
    """ Simple function that displays two passed numbers """
    
    print("There were {} numeric elements found in the file.".format(tally))
    print("The average value of the elements was determined to be {:0.3f}".format(average))
    
main()
