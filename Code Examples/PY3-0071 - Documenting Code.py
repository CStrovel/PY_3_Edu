# Author: Charles Strovel
# This program demonstrates proper docstring usage in python

# Documenting code helps maintainability. Yourself, or another
# programmer after you may need to decypher creative tricks
# or to untangle large, complex functions

# A docstring should be the very first line of code within a function
# beneath its declaration. Docstrings are used to describe what a function
# does. do not repeat the function or paramiter names.
# Docstrings appear as a discription inside tripple quotes
def myDocStringFunction():
    """This function prints an example docstring to the console"""

    print("{:*^70}".format("Docstring example"))
    print("def exampleFunction(param1, param2,...):")
    print('\t """This is an example docstring"""')
    print("")
    print("\tx x = 1")
    print("\tx = 25 + 1")
    print("\t...")

# Multiline docstrings are used when a function is larger and more
# complicated, or a function makes use of some tricky programming that
# requires explanation. Add a brief description of the function in the first line
# leave a blank line, and then add more verbose discription as needed.
def multiLineDocString():
    """This function provides an example of a multiline docstring

    This function prints a sample function using an example of a
    multiline docstring, like this one you are reading right now."""
    
    print("\n{:*^70}".format("Multiline Docstring Example"))
    print("def exampleFunction(param1, param2,...):")
    print('\t """This is an example multiline docstring')
    print("")
    print('\tThis is the description in the multiline')
    print('\tdocstring. Use this area to explain ')
    print('\tcomplicated programing techniques."""')
    print("")
    print("\tx x = 1")
    print("\tx = 25 + 1")
    print("\t...")

# code comments, just like this one, begin with a #. These are
# not read by the python interpreter and can serve to explain code
# in the same line. 
def main():
    """docstrings are read by the python interpreter

    though do not appear in output. This is useful for
    creating documentation with code parsing tools"""
    
    #we can call the two functions from inside main()
    myDocStringFunction()
    multiLineDocString()

# main function call
main()
