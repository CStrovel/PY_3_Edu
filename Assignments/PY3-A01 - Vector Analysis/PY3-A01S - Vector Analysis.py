#Author: Charles Strovel
#Written for python 3.7
#Description: Takes two sets of vector coordinators from the user
#finds their sum, their difference, and their individual magnitudes

#get the users name 
userName = input("Please enter your name: ")

#get the first vector x and y coordinates
firstX = eval(input("Please enter the x-coordinate for the first vector: "))
firstY = eval(input("Please enter the y-coordinate for the first vector: "))

#get the second vector x and y coordinates 
secondX = eval(input("Please enter the x-coordinate for the second vector: "))
secondY = eval(input("Please enter the y-coordinate for the second vector: "))

#output the users name after a line break 
print("\nThe user's name is ", userName)

#output the vector magnitudes 
print("The magnitude of the first vector is {0:.3f}".format((firstX**2 + firstY**2)**(1/2)))
print("The magnitude of the second vector is {0:.3f}".format((secondX**2 + secondY**2)**(1/2)))


#output the sum of the two vectors with a gap from the vector magnitudes 
print("\nThe sum of the two vectors is <{0:.3f}, {1:.3f}>".format(firstX+secondX , firstY+secondY))

#output the difference of the two vectors
print("The difference of the two vectors is <{0:.3f}, {1:.3f}>".format(firstX-secondX , firstY-secondY))
 
#hold command prompt until user input
input()