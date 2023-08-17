# Author: Mark Dencler
# Edited for 3.7 by Charles Strovel
# Description: This program demonstrates different mechanisms used
#   to display literal values on the screen.  The escape sequences for
#   string literals are also demonstrated.

# display a string with single quotes
print('You can display a string literal contained by single quotes.')

# display a string with double quotes
print ("You can also display a string literal with double quotes.")

# use double quotes inside of single quotes
print ('You can use "double quotes" inside of single quotes.')

# use single quotes inside of double quotes
print ("You can use 'single quotes' inside of double quotes.")

# use triple-double quotes
print ("""You can display " and ' with triple quotes.""")

# use triple-single quotes (no different besides looks)
print ('''Triple quotes can also take single quote form.''')

# use triple quotes to display multiple lines
print ('''First Line
Second Line
Third Line''')

# we can also display numeric constants
print (45)
print (45.6)
print (45.6000000)    # minimal field width by default

# Special "escape sequences" can be placed in a string literal to
# get a desired display effect.  The escape sequences are:
# \n \t \' \" and \\
print ('This is\nactually two lines')
print ('Tabs\tmove\tto\tinvisible\tvertical\tlines.')
print ('\'single quotes\' can go in string made with \'single quotes\'')
print ("\"double quotes\" can go in a string made with \"double quotes\"")
print ('How many backslashes display? \\\\\\\\\\')

input('Press Any Key To Continue')

