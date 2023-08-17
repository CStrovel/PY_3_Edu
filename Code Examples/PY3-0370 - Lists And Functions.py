# Author: Mark Dencler
# Modified for python 3.7 by Charles Strove
# Description: This program demonstrates the way that lists interact with functions.

def main():
    # begin by creating a list with some numbers
    myList = [10, 20, 30, 40, 50]

    # PASSING A LIST INTO A FUNCTION (NATURAL REFERENCE PASS)
    # display the contents of the list
    print("{:*^80}".format(" Passing a List "))
    print("BEFORE CALLING THE 1ST FUNCTION CALL, THE LIST CONTAINS:")
    print(myList)
    print("")

    # When making a list, the list's identifier acts as a reference to the contents
    # of the list. That means that any function calls that get made will pass in the
    # actual reference to the original list, not a copy.
    doubleListContents(myList)

    # display the contents of the list after the function call
    print("AFTER CALLING THE 1ST FUNCTION CALL, THE LIST CONTAINS:")
    print(myList)
    print("")

    # PASSING A LIST INTO A FUNCTION (FAKING A PASS BY VALUE)    
    # create a list with some words in it
    fruitList = ['Bananna', 'Apple', 'Lemon', 'Lime', 'Cherry', 'Peach']

    # display the list before the function call
    print("{:*^80}".format(" Fake Pass by Value "))
    print("BEFORE CALLING THE 2ND FUNCTION, THE LIST CONTAINS:")
    print(fruitList)
    print("")

    # If we want to get pass-by-value behavior when passing a list into
    # a function, we must make a copy of the list internally...
    displayAlphabetizedList(fruitList)
    print("")

    # display the contents of the list after the function call
    print("AFTER CALLING THE 2ND FUNCTION, THE LIST CONTAINS:")
    print(fruitList)
    print("")

    # RETURNING A LIST FROM A FUNCTION
    # If a list is made within the body of a function, it does not lose scope
    # when that function no longer exits.  This means the list reference can 
    # be returned and used in other places within the program
    print("{:*^80}".format(" Capturing a Returned List "))

    # create an empty list reference
    zeroList = []

    # display the empty list
    print("BEFORE THE 3RD FUNCTION CALL, THE LIST CONTAINS:")
    print(zeroList)
    print("")

    # call a funcion that will make a list of the designated size that
    # contains all zeros
    zeroList = makeZeroList(10)

    # display the list after the function call
    print("AFTER THE 3RD FUNCTION CALL, THE LIST CONTAINS:")
    print(zeroList)
    print("")


# FUNCTION BODYS
def doubleListContents(someList):
    """ doubles the values in a numeric list"""

    # for each element in the list
    for element in range( len(someList) ):
        # double each value in the list
        someList[element] *= 2

def displayAlphabetizedList(alphabetizeMe):
    """ alpabatizes a list after creating local copy"""

    # make a local copy of the list that was passed in
    tempList = []
    for element in alphabetizeMe:
        tempList.append(element)

    # sort the list
    tempList.sort()

    # display the alphabetized list
    print("INSIDE THE 2ND FUNCTION (AFTER SORTING), THE LIST CONTAINS")
    print(tempList)

def makeZeroList(listSize):
    """ generates a list of a custom size """

    # establish an internal list reference to an empty list
    returnMe = []

    # create the list and fill it with zeros
    for element in range(listSize):
        returnMe.append(0)

    # return the newly populated list reference
    return returnMe


# Begin MAIN()
main()
