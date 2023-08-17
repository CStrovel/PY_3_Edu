# Author: Mark Dencler
# Modified for python 3.7 by charles strovel 
# Description: This program demonstrates formatted output.

# USING MULTIPLE PRINTS TO SEPERATE OUTPUT
# we can seperate multiple outputs by using different print statements
myName = 'Mark Dencler'
print('My name is ')
print(myName)
print('')                # blank space

# notice that a stand-alone print statement automatically adds a
# newline character to the end of the output


# USING COMMAS IN PRINT STATEMENTS
# we can also use a comma to seperate multiple values on the same print
print('My name is', myName)

# notice that the comma automatically puts a space between the
# two values in the display

# the comma can also be used to suppress the newline behavior of print
# (the space is still placed at the end of the text)
print ('This will display without a newline',)
print ('Look!  It\'s on the same line')


# USING THE STRING CONCATENATION OPERATOR IN PRINT STATEMENTS
print ('My name is ' + myName)

# notice the + does not add the space between the two values
# in the display... you can only concatenate string with other strings
#print 'I wish I had $' + 1000000 + ' to spend on candy.'   # ERROR


# MIXING DATA TYPES IN PRINTS (use the comma)
numberName = 'pi'
numberFloatValue = 3.14
numberIntValue = 3

# different data types can be mixed with commas
# use the blackslash to initiate a line continuation
print ('The number', numberName + ' is about', numberFloatValue, \
      'but as an \'int\' that is', numberIntValue, '\n')


# USING A FORMAT STRING TO FORMAT OUTPUT
# you can also use a format string to make output appear however you like
# this method of formatting is moving towards deprication, however it is very 
# common to see strings formated this way, so you should be familiar with it. 
print ('The number %s is about %f, but as an \'int\' that is %d' % (numberName, numberFloatValue, numberIntValue))

# use the line continuation to make things more managable
print( 'The number %s is about %f, but as an \'int\' that is %d' % \
      (numberName, numberFloatValue, numberIntValue))

# USING A FORMAT SPECIFIER TO SET FIELD WIDTH, PRECISION, AND JUSTIFICATION
crazyFloat = 1.23456789

# we can specify a field width (default justification is right)
print( '%15f' % (crazyFloat))

# we can override the justification to be left
print( '%-15f' % (crazyFloat))

# we can tack together multiple format strings and argument lists as well
one = 1
two = 2
three = 3
print ('%d %d %d' % (one, two, three))
print ('%d' % (one), "%d" % (two), """%d""" % (three))  # SAME THING AS LAST LINE

# we can set the precision display for floats by placing a format specifier after the dot
print("%.2f" % crazyFloat)
print("%.3f" % crazyFloat)  # STANDARD ROUNDING IS USED

# we can combine all of these ideas to make attractive displays
hisMoney = 24.457
herMoney = 43.43
theDogsMoney = 110.44345
videoGamesAndAssortedElectronicsMoney = 2000
print("Look how all the decimal points line up:")
print('$%8.2f\n$%8.2f\n$%8.2f\n$%8.2f\n' % \
      (hisMoney, herMoney, theDogsMoney, videoGamesAndAssortedElectronicsMoney))
input()