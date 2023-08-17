# Author: Charles Strovel
# Description: Demonstrates some basic characteristics of python strings  

def basicStrings():
    """demonstrates basic python string characteristics

    such as imutability, string indexing, and length()"""

    # declare a string
    myString = 'Hello, this is a string.'

    # Strings are immutable objects, which means they cannot be changed.
    # When we make an assignment to change the value of the string, a completely
    # new string is created and linked to the old string's reference.
    myString = 'Here is another string.  It is replacing the old one.'

    # After the previous statement, the old string is still sitting around
    # in memory, but no variavles are referencing it anymore.  It will be
    # collected by a garbage collector and the RAM is was existing in
    # will be reclaimed.

    # we can get access to the length of the string using the len() function.
    print('The string contains {} characters.'.format(len(myString)))
    print("")

    # Even though a string is immutable, we can still look at the individual
    # chanracters that make up the string with the 'in' keyword.
    myString = 'tiny string'
    for holder in myString:
        print("holder contains: {}".format(holder))
    print("")

    # we can also iterate through the characters in the string one at a time
    # using index notation.  By using the len() function in conjunction with
    # the loop syntax, we can safely interate through the characters.
    for index in range( len(myString) ):
        print('myString[{}] contains: {}'.format(index, myString[index]))
    print("")

    # we can use a negative index to look at the contents in reverse order
    for index in range(-1, -1 * len(myString) - 1, -1 ):
        print('myString[{}] contains: {}'.format(index, myString[index]))
    print("")

    # if a bad index is used, an exception will be raised
    for index in range(12):
        try:
            print('myString[{}] contains: {}'.format(index, myString[index]))
        except IndexError:
            print('EXCEPTION: You cannot access index {}'.format(index))
    print("")

    # DO NOT attempt to change the values in the string with the index
    # operators.  This will result in an exception.
    try:
        myString[0] = 'g'
    except TypeError:
        print('EXCEPTION: You cannot mutate a string.')
    print("")

def stringSlicing():
    """Provides examples for slicing strings using list notation"""

    # STRING SLICING
    # A string can be sliced to return a subset of its contents.  The slicing
    # operation will create a new string and return a reference to it.  This
    # reference can be captured by a new variable.
    myString = 'abcdefg'
    slic = ""

    # basic slice (begin index : end index) - get all the characters between
    # two indexes (not including the last index)
    slic = myString[2:4]
    print('The slice [2:4] of string {0} contains: {1}'.format(myString, slic))
    print("")

    # end slice (begin index :) - get everything from a specific index
    # to the end of the string
    slic = myString[5:]
    print('The slice [5:] of string {0} contains: {1}'.format(myString, slic))
    print("")

    # beginning slice (: end index) - get everything up to a specific index
    # (not including the last index)
    slic = myString[:4]
    print('The slice [:4] of string {0} contains: {1}'.format(myString, slic))
    print("")

    # full slice ( : ) - get it all
    slic = myString[:]
    print('The slice [:] of string {0} contains: {1}'.format(myString, slic))
    print("")

    # stepping slice (begin index : end index : step) - get characters between
    # two indexes (not including the last index), with an offset.
    slic = myString[1:7:2]
    print('The slice [1:7:2] of string {0} contains: {1}'.format(myString, slic))
    print("")

    # open stepping splice ( : : step) - combine stepping with a possible open
    # index
    slic = myString[::2]
    print('The slice [::2] of string {0} contains: {1}'.format(myString, slic))
    print("")

def stringKeyWords():
    """Demonstrates simple keywords to identify if a string contians another string"""

    # IN and NOT IN
    # the 'in' and 'not in' keywords can be used to test if a substring
    # is contained within a parent string.
    myString = 'dog cat hampster monkey'
    if 'dog' in myString:
        print('The string contains the substring "dog".')
    else:
        print('The string does not contain the substring "dog".')

    # a similar construct can be used to test for the negation
    # of the previous test
    if 'dog' not in myString:
        print('The string does not contain the substring "dog".')
    else:
        print('The string contains the substring "dog".')

def main():
    # Basic characteristics and string indexing
    basicStrings()
    # slicing strings using index and stepping
    stringSlicing()
    # in and not in for determining if a string contains another string 
    stringKeyWords()

main()