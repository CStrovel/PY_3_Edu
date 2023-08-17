#Author: Charles Strovel
#written for python 3.7
#Discription: This program introduces formatting 
#strings with replacement fields and .format()
firstName = "Charles"
lastName = "Strovel"

#Python can use a powerful string method, format()
print('Hello, my name is {0} {1}'.format(firstName, lastName))

#All strings can use the format method()
fString = "Hello, my name is {0} {1}"
print(fString.format(firstName, lastName))
print("")

#format() searches a string for replacement fields, contained in curly braces 
#then replaces them with the arguments passed to it positionally 
fString = "the prime numbers are {},{},{},{},{},{}"#can also be written as {0}{1}{2}...
print(fString.format(2,3,5,7,11,13))

#the index of each replacement field can be set manually
fString = "the prime numbers are {2},{3},{0},{1},{5},{4}"
print(fString.format(2,3,5,7,11,13))

#or format() can use key word arguments 
fString = "the prime numbers are {first},{second},{third},{fourth},{fifth},{sixth}"
print(fString.format(sixth = 2, fifth = 3, fourth = 5, third = 7, second = 11, first = 13))

#format() can be used with escaped characters for further string formatting 
fString = "{}first line{}second line{}third line{}"
print(fString.format('\n','\n','\n','\n',))

#format() and repalcement fields can also be used to format how numbers are displayed 
#Format specifiers come at the end of a replacement field just before the close bracket
#use f for float, d for integers, and s for strings. The number to the right of the decimal
#point determines to what place the number is displayed 
tenths, hundredths, thousandths, tenThousandths = '{a:1.1f}\n','{a:.2f}\n','{a:.3f}\n','{a:.4f}\n'
pi = 3.14159
print(("Pi progression:\n" + tenths + hundredths + thousandths + tenThousandths).format(a = pi))

#Replacement fields can also be padded and aligned. A number between the colon and the decimial point
#determines field width, <, ^, and > are used to indicate left, center, or right justification 
l, c, r = "left","center","right"
print("|{0:<50s}|\n|{1:^50s}|\n|{2:>50s}|\n".format(l,c,r))

#we can even change the character used to pad a replacement field's content
#by adding the character between the colon and the less than/greater than/carrot 
print("|{0:*<50s}|\n|{1:%^50s}|\n|{2:~>50s}|".format(l,c,r))
input()