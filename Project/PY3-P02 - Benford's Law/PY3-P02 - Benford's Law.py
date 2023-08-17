# Written by Charles Strovel
# Provides a solution to analizing data files with benfords law 

import math
# Path for data files
PATH = "P02_DataFiles\\"
# File list, may be appended as needed 
IN_FILE_LST = []
IN_FILE_LST.append("P02_DataFile_0.dat")
IN_FILE_LST.append("P02_DataFile_1.dat")
IN_FILE_LST.append("P02_DataFile_2.dat")
IN_FILE_LST.append("P02_DataFile_3.dat")
IN_FILE_LST.append("P02_DataFile_4.dat")
IN_FILE_LST.append("P02_DataFile_5.dat")
IN_FILE_LST.append("P02_DataFile_6.dat")
IN_FILE_LST.append("P02_DataFile_7.dat")
IN_FILE_LST.append("P02_DataFile_8.dat")
IN_FILE_LST.append("P02_DataFile_9.dat")

def benfordProbs():
    """Caculates benford probabilities dynamically
    
    it would also be fairly reasonable to manually input benford
    numbers as a global list
    """
    # Variables
    benList = []

    for i in range(9):
        benList.append(math.log10(1 + 1/(i + 1)))

    return benList

def readInFileStr(fileName):
    """Reads an input file, returning a string of its contents""" 
    # Variables
    inFileStr = "" 

    # open the file for reading using the with command 
    with open(fileName, "r") as inFile:
        # read input file line by line into a list 
        inFileStr = inFile.read()

    return inFileStr

def checkListNumeric(numList):
    """Checks each list entry for purly numeric data. Dumps any bad entries"""
    # Variables 
    rtrnLst = []
    
    # iterate through incoming list 
    for num in numList:
        # Append entry into return list if it's numeric 
        if str(num).isnumeric:
            rtrnLst.append(num)
    
    return rtrnLst

def getTally(numList):
    """Tallys the number of times each digit appears as a leading number"""
    # Variables
    tallyList = [0,0,0,0,0,0,0,0,0]
    capture = ""

    # iterate through incoming list
    for num in numList:
        # capture the leading number
        capture = str(num)[0]
        # the captured number can now be used to find the index to incriment
        tallyList[int(capture) - 1] += 1 

    return tallyList 

def averageList(numList, denominator):
    """Averages all numbers in a list, returning a list with corisponding averages"""
    # Variables
    rtrnLst = []

    # iterate through incoming list
    for num in numList:
        try:
            rtrnLst.append(num / denominator)
        
        except: 
            print("averageList() encountered a problem. Value integrety comprimised.")
            # allows program to keep running 
            rtrnLst.append(1)
    
    return rtrnLst

def benfordOffset(avgLst, benProbs):
    """determines the absolute value difference between an average

        and it's bendford probability
    """
    # Variables
    offsets = []

    # iterate through benford list 
    for i in range(len(benProbs)):
        # append the absolute value of list average - probability 
        offsets.append(abs(avgLst[i] - benProbs[i]))

    return offsets 

def displayFileResults(fileName, tallyLst, avgLst, offsetLst):
    """Presents the analysis results of each individual file neatly"""
    # Variables 
    line =  "{0}{1:-<57}{0}"
    line2 = "|{0:-<11}+{0:-<8}+{0:-<16}+{0:-<19}|".format("")
    header = "| {:<10}| {:<7}| {:<15}| {:<18}|"
    data = "| {:<10}| {:<7}| {:<15.5f}| {:<18.3f}|"
    
    # pre load file name string so its easier to ajust field width
    fileStr = "|{:<57}|".format(" Results for file: {}".format(fileName)) 
   
    # begin printing table with header 
    print(line.format("+",""))
    print(fileStr)
    print(line.format("|",""))
    print(header.format("Digit", "Count", "Probability", "Benford Offset"))
    print(line2)
    
    # print data 
    for i in range(len(tallyLst)):
        print(data.format(i + 1, tallyLst[i], avgLst[i], offsetLst[i]))
    
    # end table 
    print(line.format("+",""))

def fraudCheck(fileLst, fCoefficent):
    """ Displays file names with their associate forge coefficent"""
    # Variables 
    capLine = "+{:-<57}+".format("")
    header = "| {:<27}| {:<27}|".format("File Name", "Fraud Coefficent")
    data = "| {:<27}| {:<27.3f}|"
    
    # Print table header
    print("\n" + capLine)
    print(header)
    print(capLine)

    # Loop to display data
    for i in range(len(fileLst)):
        # Print a data field 
        print(data.format(fileLst[i], fCoefficent[i]))

    # Close the table
    print(capLine)

def main():
    
    # Variables  
    benProbs = benfordProbs()
    forgeCoefficent = [] 

    # Iterate through the list of files 
    for fileName in IN_FILE_LST:
        # Read in the string from file, strip ends and split into list
        numLst = readInFileStr(PATH + fileName).strip("\n").split("\n")

        # Check file for only numeric characters, discard entries that are not
        numLst = checkListNumeric(numLst)

        # tally leading numbers. Remember that index of returned list is
        # shifted - 1 from the integer actually represented. 
        tallyLst = getTally(numLst)

        # average the appearance of each number
        avgLst = averageList(tallyLst, len(numLst))

        # retrieve benford offsets 
        offsetLst = benfordOffset(avgLst, benProbs)

        # Display results for the file
        displayFileResults(fileName, tallyLst, avgLst, offsetLst)
    
        # append fraud coefficent to list 
        forgeCoefficent.append(sum(offsetLst))


    # final display, file name with coefficents 
    fraudCheck(IN_FILE_LST, forgeCoefficent)
main()
