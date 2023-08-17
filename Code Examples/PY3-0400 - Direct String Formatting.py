# Author: Mark Dencler
# Modified for python 3.7 by Charles Strovel
# Description: This program demonstrates "sys.stdout.write" and other
#              low-level IO instructions for output.

import sys

def main():
    # TECHNIQUE #1
    # When 'print()' operates, it is actually shielding a method call to a lower
    # level object that can be found at "sys.stdout".  We can evoke this method
    # directly to get exact output on the screen that would not normally
    # be possible (for example displaying output without a newline and
    # no space after the last character.
    sys.stdout.write("This string was written using a direct call to sys.stdout.write")
    # NOTE: notice there is no newline or space after the last character
    print("")
    print("")

    # The limitation of a method call like this is that conversion characters
    # or other similar mechanisms cannot be used to generate robust output.


    # TECHNIQUE #2
    # we can also build custom strings using the built-in % operator support for strings
    print("MANIPULATING INDEPENDENT STRINGS USING THE % OPERATOR")
    tempString = "Here is the %dnd string that uses %s characters."
    newString = tempString % (2, 'conversion')
    sys.stdout.write("tempString: ")
    sys.stdout.write(tempString)
    sys.stdout.write('\n')
    sys.stdout.write("newString: ")
    sys.stdout.write(newString)
    sys.stdout.write('\n\n')

# Begin MAIN()
main()
