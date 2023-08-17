# Author: Mark Dencler
# Modified for python 3.7 by Charles Strovel 
# Description: This program demonstrates some of the common string methods.

def examMethods():
    """ Demonstrates different methods that can be used to examine a strings content"""

    # In this example variables are used to hold the appropriate strings, but
    # the run time examples are displayed as string literals. Keep in mind that these 
    # methods work with both, IE numString.isalnum() is functionally equivalant to 
    # '123456'.isalnum() 
    numString = '123456'
    alpString = 'abcdABCD'
    mixString = 'abc#*^123' 

    # EXAMINATION METHODS
    # isalnum() - returns true if the string contains only letters and numbers 
    print("'{}'.isalnum() = {}".format(numString, numString.isalnum()))
    print("'{}'.isalnum() = {}".format(alpString, alpString.isalnum()))
    print("'{}'.isalnum() = {}".format(mixString, mixString.isalnum()))
    print("")

    # isalpha() - returns true if the string contains only letters
    print("'{}'.isalpha() = {}".format(numString, numString.isalpha()))
    print("'{}'.isalpha() = {}".format(alpString, alpString.isalpha()))
    print("'{}'.isalpha() = {}".format(mixString, mixString.isalpha()))
    print ("")

    # isdigit() - returns true if the string contains only digits
    print("'{}'.isdigit() = {}".format(numString, numString.isdigit()))
    print("'{}'.isdigit() = {}".format(alpString, alpString.isdigit()))
    print("'{}'.isdigit() = {}".format(mixString, mixString.isdigit()))
    print("")

    # islower() - returns true if the string contains only little letters
    print("'{}'.islower() = {}".format(numString, numString.islower()))
    print("'{}'.islower() = {}".format(alpString, alpString.islower()))
    print("'{}'.islower() = {}".format(mixString, mixString.islower()))
    print("")

    # isspace() - returns true if the string only contains whitespace
    print("'{}'.isspace() = {}".format(numString, numString.isspace()))
    print("'{}'.isspace() = {}".format(alpString, alpString.isspace()))
    print("'{}'.isspace() = {}".format(mixString, mixString.isspace()))
    print("")

    # isupper() - returns true if the string only contains big letters
    print("'{}'.isupper() = {}".format(numString, numString.isupper()))
    print("'{}'.isupper() = {}".format(alpString, alpString.isupper()))
    print("'{}'.isupper() = {}".format(mixString, mixString.isupper()))
    print("")

    # endswith(string) - returns true if the string ends with the argument
    print("'{}'.endswith('456') = {}".format(numString, numString.endswith('456')))
    print("")

    # startswith(string) - returns true if the tsring begins with the argument
    print ("'{}'.startswith('123') = {}".format(numString, numString.startswith('123')))
    print("")

    # find(string) - returns the smallest index where the argument can be
    # fully found within the string.  will return -1 is the argument
    # cannot be found.
    print("'{}'.find('456') = {}".format(numString, numString.find('456')))
    print("'{}'.find('456789') = {}".format(numString, numString.find('456789')))
    print("")

def mutationMethods():
    """Demonstrates string class methods that can return a mutated string"""

    startWithMe = '  ***abcABC***   '
    printMe = ""

    # lower() - returns a string in only lower case letters
    printMe = startWithMe.lower()
    print("'{}'.lower() = '{}'".format(startWithMe, printMe))
    print("")

    # upper() - returns a string in only big letters
    printMe = startWithMe.upper()
    print("'{}'.upper() = '{}'".format(startWithMe, printMe))
    print("")

    # strip() - removes whitespace from the beginning and end of the string
    printMe = startWithMe.strip()
    print("'{}'.strip() = '{}'".format(startWithMe, printMe))
    print("")

    # NOTE: This function has sibling functions lstrip() and rstrip() that
    # only apply the behavior to the respective left or right side of
    # the string.

    # strip(character) - returns a string with the designated character
    # removed from the beginning and end of the string. Resolve from left to right. 
    printMe = startWithMe.strip().strip('*')
    print("'{}'.strip().strip('*') = '{}'".format(startWithMe, printMe))
    print("")

    # NOTE: This function has sibling functions lstrip() and rstrip() that
    # only apply the behavior to the respective left or right side of
    # the string.

    # replace(oldString, newString) - returns a string with all instances
    # of the old string replaced by the new string
    printMe = startWithMe.replace('abc', "ABC")
    print("'{}'.replace('abc','ABC') = '{}'".format(startWithMe, printMe))
    print("")

    # REPETITION OPERATIONS
    # The multiplication symbol can be used together with a string to
    # generate a result string with multiple instances of the original
    # string.  This can be used to streamline to coding of a string
    # that has a repetitious nature to it.
    startWithMe = 'abc'
    printMe = startWithMe * 10
    print("'{}' * 10 = '{}'".format(startWithMe, printMe))
    print("")

def main():
    """ Demonstrates string methods in two parts, exam methods and mutation methods"""

    # Technically, strings are classes, which means we have access to the
    # methods that belong to that class.  We can use these methods to
    # make modifications to the string objects and examine their contents.
    # Methods that help you look at what's in a string 
    examMethods()

    # Methods that help you change or retrieve parts of a string
    # keep in mind strings are imutable, so these methods often return 
    # strings that need to be captured 
    mutationMethods()

main()
