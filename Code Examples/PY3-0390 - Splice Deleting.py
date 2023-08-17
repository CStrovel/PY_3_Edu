# Author: Mark Dencler
# Modified for pythong 3.7 by Charles Strovel 
# Description: This program demonstrates the use of splices to delete
#              elements from a list.

def main():
    # DELETING THINGS USING SPLICES
    # create a list that contains all of the integers between -10 and 10
    myList = []
    
    for x in range(-10,11):
        myList.append(x)

    # display the list
    print("INITIAL LIST:")
    print(myList)
    print("")

    # use a splice to delete all of the negative elements
    del myList[0:10]

    # display the list
    print("AFTER DELETING myList[0:10]")
    print (myList)
    print ("")

    # use a splice to delete all of the even elements in the list
    del myList[0:11:2]

    # display the list
    print ("AFTER DELETING myList[0:11:2]")
    print (myList)
    print ("")

    # DELETING THINGS USING THE INDEX METHOD
    # create a list of random letters between A and C
    letterList = ['A', 'C', 'B', 'C', 'A', 'C', 'A', 'B', 'B', 'C', 'A']

    # display the list
    print ("INITIAL LETTER LIST:")
    print (letterList)
    print ("")

    # use the index operator to delete all instances of the letter A
    targetFound = True
    while targetFound == True:
        try:
            deleteIndex = letterList.index('A')

        # Exception occurs if 'A' is not found in the list
        # We can assume that 'A' was found in the list if ValueError is not thrown 
        except ValueError:
            print("The last instance of 'A' was deleted...")
            print("")
            targetFound = False 

        # Only delete if target found is still true. IE ValueError has not occured
        # otherwise we will generate another error 
        if targetFound: 
            del letterList[deleteIndex]

    # display the list
    print("AFTER DELETING 'A's LETTER LIST:")
    print(letterList)
    print("")
            
# Begin MAIN()
main()
