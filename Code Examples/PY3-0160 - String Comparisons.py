# Author: Mark Dencler
# Edited for 3.7: Charles strovel
# Description: This program demonstrates string comparison operations.

def main():
    String_1 = 'Alice'
    String_2 = "Bob"
    String_3 = 'alice'
    String_4 = 'bob'
    String_5 = 'Dog'
    String_6 = "Doggies"

    # In Python, we can compare two string directly with the quantitative
    # comparison operators.  The result will be similar to placing the
    # strings in alphabetical order based on the comparisons of the ASCII
    # codes associate with the letters.  If two strings are identical
    # to a point, the shorter string is considered to be of lesser value
    # than the longer one.
    CompareStrings(String_1, String_2)
    CompareStrings(String_3, String_2)
    CompareStrings(String_5, String_6)
    CompareStrings(String_4, String_2)
    CompareStrings(String_3, String_3)


    input()

def CompareStrings(stringOne, stringTwo):
    if stringOne > stringTwo:
        print('The string "' + stringOne + '" is greater than "' + stringTwo + '".')
    elif stringOne < stringTwo:
        print('The string "' + stringOne + '" is less than "' + stringTwo + '".')
    else:
        print('The string "' + stringOne + '" is equal to "' + stringTwo + '".')


# Begin MAIN()
main()
