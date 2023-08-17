# Author: Mark Dencler
# Edited for python 3.7 by Charles Strovel 
# Description: This program demonstrates basic list manipulation.

def main():
    """ Demonstrates basic list syntax and common usage"""
    
    # basic syntax for creating a list 
    myList = [1, 2, 3, 4, 5]

    # print() has functionality for displaying the raw contents of a list
    print(myList)
    print("")

    # lists can contain multipule data types at once
    myList = [1, "two",3.1, True]
    print(myList)
    print("")

    # We can get the number of elements in the list in the same way
    # that we got the size of a string.
    print("The list contains {} elements.".format(len(myList)))
    print("")

    # We can iterate over a list in the same way that we iterate over
    # a string.

    # using the 'in' keyword
    for temp in myList:
        print("The variable temp contains: {}".format(temp))
    print("")

    # using an index - keep in mind that the first index value is zero and
    # the last index value is one less than the size of the list
    for index in range(0, len(myList)):
        print("myList[{}] = {}".format(index, myList[index]))
    print("")

    # slicing operations are also supported for lists in the same way
    # they were supported for strings
    sliceList = myList[0:4:3]
    for index in range(0, len(sliceList)):
        print("sliceList[{}] = {}".format(index, sliceList[index]))
    print("")

    # another list example, don't forget lists can hold all primative data types! 
    stringList = ['Iggy', 'Lemmy', 'Morton', 'Wendy']

    # we can use the 'in' and 'not in' keywords to detect the presence
    # of a specific value within the list
    if 'Iggy' in stringList:
        print('Iggy was found in the list.')
    else:
        print('Iggy was not found int he list.')

    if 'Roy' not in stringList:
        print('Roy was not found in the list.')
    else:
        print('Roy was found in the list.')
    print("")

    # Lists are mutable objects, which means their contents can be changed.
    # When an individual portion of a list is changed, that small piece
    # of the list is singled out and modified.

    # we can modify the contents of a list by changing an indexed value directly

    stringList[0] = 'Ludwig'
    print(stringList)

    # We can also append to a list, demonstrated in the next sample code. 

main()
