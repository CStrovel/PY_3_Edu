# Author: Charles Strovel
# Description: This program reads in and catalogs unique words from a txt
# verion of the book of genesis 

# Global Constants 
IN_FILE_NAME = "PY3-A07S-Genesis.txt"
OUT_FILE_NAME = "PY3-A07S-GenisisWords.txt"

def readInFileStr(fileName):
    """Reads an input file, returning a string of its contents""" 
    # declare list
    inFileStr = "" 

    # open the file for reading using the with command 
    with open(fileName, "r") as inFile:
        # read input file line by line into a list 
        inFileStr = inFile.read()

    return inFileStr

def purify(termLst): 
    """ removes punctuation and numerical data, returning only a alph char word list""" 
    # variables
    rtrnList = [] 

    # iterate through the list to grab each word 
    for term in termLst:
        # iterate through the term to check each letter for alpha character
        # Reset capture string 
        captureStr = ""

        # iterate through each letter in the word 
        for letter in term:
            # check to see if the letter is alphanumeric 
            if letter.isalpha():
                captureStr += letter

        # Append capture string into a new list
        rtrnList.append(captureStr.upper())
    
    return rtrnList 

def organize(termList):
    """ Creates an ordered list with no duplicates or empty spaces
    
        This could easly have been done in purify() but is broken out 
        for clarity and to demonstrate different functionality
    """
    # variables 
    rtrnList = []

    # iterate through passed list
    for term in termList:
        # check to see if the word is already in rtrnList, and if it's blank
        if term and not term in rtrnList:
            rtrnList.append(term)

    # re order the list alphabetically 
    rtrnList.sort()

    return rtrnList 

def writeOutFile(outList, outFile):
    """ saves a list to file """

    # open file for writing
    with open(outFile, "w") as oFile:
        # iterate through elements in list
        for item in outList:
            # save each item to a line in the file 
            oFile.write(item + "\n")

    return 

def main():
    # declare variables 
    genList = [] 

    # take the string from readInFileStr and split it 
    genList = readInFileStr(IN_FILE_NAME).split(" ")
    
    # remove punctuation, numbers, and move all words to upper case 
    genList = purify(genList)

    # remove duplicates and empty strings, return an ordered list 
    genList = organize(genList)

    # write the output file 
    writeOutFile(genList, OUT_FILE_NAME)

main()
