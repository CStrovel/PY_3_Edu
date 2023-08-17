# Author: Mark Dencler
# Modified for python 3.7 by Charles Strovel 
# Description: This program demonstrates some common methods of lists.

def main():
    myList = ['Alice', 'Bob', 'Charlie', 'Dana', 'Edwin']

    # display the list
    print(myList)
    print("")

    # append() - add an element to the end of the list
    myList.append('Frank')
    print(myList)
    print("")

    # del - the 'del' keyword can be used to remove an item from
    # the list
    del myList[0]    # delete the first element
    print(myList)
    del myList[len(myList) - 1]   # delete the last element
    print(myList)
    print("")

    # index(value) - index can be used to get the index of a specific
    # value within the list
    searchStr = 'Dana'
    try:
        index = myList.index(searchStr)
    
    # the error thrown by a liste item that is not found by index is a ValueError 
    except ValueError:
        print('The string "{}" can not be found.'.format(searchStr))
        print("")
        # index will either contain the index value where the list item was found,
        # or False if an exception occured, allowing us to use it as a flag to 
        # display (or not display) results 
        index = False 


    if index: # check if index has a value other than False in it. 
        print('The string "{}" can be located at index {}'.format(searchStr, index))
        print("")

    # NOTE: This will raise an exception if an item cannot be matched.
    searchStr = 'George'
    
    try:
        index = myList.index(searchStr)

    except ValueError:
        print('The string "{}" can not be found.'.format(searchStr))
        print("")
        index = False 

    if index:
        print('The string "{}" can be located at index {}'.format(searchStr, index))
        print("")

  # insert(index, value) - we can put new items in the list with insert()
    myList.insert(2, 'Mark')
    print(myList)
    myList.insert(2, 'David')
    print(myList)
    myList.insert(1, 'Jean')
    print(myList)
    print("")

    # sort() - we can sort the last based on quantitative comparisons
    print('BEFORE SORTING')
    print(myList)
    myList.sort()
    print('AFTER SORTING')
    print(myList)
    print("")

    # reverse() - we can reverse the order of the list
    print('BEFORE REVERSE')
    print(myList)
    myList.reverse()
    print('AFTER REVERSE')
    print(myList)
    print("")

    # the min() and max() functions can be used to report the highest
    # and lowest values contained in the list
    print('The highest value in the list is: {}'.format(max(myList)))
    print('The lowest value in the list is : {}'.format(min(myList)))
    print("")

    # BE CAUTIOUS OF LIST COPIES... YOU WILL SIMPLY GET TWO REFERENCES
    # POINTING TO THE SAME LIST
    myOtherList = myList
    print("")
    print('myList     : {}'.format(myList))
    print('myOtherList: {}'.format(myOtherList))
    del myOtherList[0]
    del myOtherList[0]
    del myOtherList[0]
    print('myList     : {}'.format(myList))
    print('myOtherList: {}'.format(myOtherList))
    print("")

    # To get a true copy of the list, we must copy the characters one at a time.
    # The string concatenation operator returns copies of concatenated lists,
    # so we can use that to our advantage when we need to make a true copy.
    print('myList     : {}'.format(myList))
    print('myOtherList: {}'.format(myOtherList))
    myOtherList = [] + myList     # empty list + list we want to copy
    del myOtherList[0]
    del myOtherList[0]
    del myOtherList[0]
    print('myList     : {}'.format(myList))
    print('myOtherList: {}'.format(myOtherList))
    print("")
    
main()