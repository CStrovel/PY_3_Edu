#Author: Charles Strovel
#Discription: This program takes input from a user for the length and height of various
#animal pens, then computes the area of each and the total area of all pens together.
#this assignment is to teach students prompt formatting and appropriate use of functions. 

#declare global variables
cowHeight = 0.0
cowArea = 0.0
cowPerimeter = 0.0
rhinoArea = 0.0
rhinoPerimeter = 0.0
turtleHeight = 0.0
turtleArea = 0.0
turtlePerimeter = 0.0 
birdArea = 0.0
birdPerimeter = 0.0
PI = 3.14159
totalArea = 0.0
totalExternalPerimeterr = 0.0
totalFenceing = 0.0

def main():
    #get length and height of cow pen from user
    #note that this cowHeight is only local 
    cowHeight = eval(input("Please enter moo-cow pen height\t\t: "))
    cowLength = eval(input("Please enter moo-cow pen length\t\t: "))
    
    #calculate cow pen perimeter and area
    #useing positional arguments 
    mooCow(cowHeight, cowLength)

    #get length and height of rhino common ground from user
    rhinoHeight = eval(input("Please enter rhino common ground height\t: "))
    rhinoLength = eval(input("Please enter rhino common ground length\t: "))

    #Calculate rhino common ground perimeter and area
    #using keyword arguments (kwargs)
    rhinoPen(height = rhinoHeight, length = rhinoLength)

    #get length and height of turtle petting area from user
    turtleHeight = eval(input("Please enter turtle petting area height\t: "))
    turtleLength = eval(input("Please enter turtle petting area length\t: "))

    #calculate turtle petting area perimeter and area
    #using a combination of kwargs and positional args
    turtlePettingArea(turtleHeight, length = turtleLength)

    #get radius of the bird cage from user
    radius = eval(input("Please enter radius of the bird cage\t: "))

    #clculate area and perimeter of the bird cage 
    #using a positional arg 
    birdCage(radius)
    
    #calculate total area and perimeters 
    calcData()

    #display measurements in a pleasing way
    displayMeasurements()
    
#Calculate cow pen perimeter and area----------------------------------
#puplates globals before returning ------------------------------------
def mooCow(height, length):
    #retrieve global variables
    global cowHeight
    global cowArea 
    global cowPerimeter

    #move height into cowHeight global 
    cowHeight = height 

    #calculate and assign area and perimeter 
    cowArea = height * length 
    cowPerimeter = height * 2 + length * 2 

#calculates the area and perimeter of the rhino grounds----------------
#populates globals before returning------------------------------------
def rhinoPen(height, length):
    #retrieve global variables
    global rhinoArea
    global rhinoPerimeter

    #Caculate and populate
    rhinoArea = height * length
    rhinoPerimeter = height * 2 + length * 2 

#calculates the area and perimeter of trutle petting area--------------
#populates globals before returning------------------------------------
def turtlePettingArea(height, length):
    #retrieve global variables
    global turtleArea
    global turtlePerimeter
    global turtleHeight

    #caculate and populate
    turtleHeight = height  
    turtleArea = height * length
    turtlePerimeter = height * 2 + length * 2

#calculates the area and perimeter of the bird cage-------------------
#populates globals before returning-----------------------------------
def birdCage(rad):
    #retrieve global variables
    global birdArea
    global birdPerimeter
    global PI

    #calculate and populate
    birdArea = PI * rad ** 2 
    birdPerimeter = 2 * PI * rad

#calculates total perimeters (external and all) -----------------------
# as well as total area-----------------------------------------------
def calcData():
    #retrieve global variables 
    global turtleArea
    global turtlePerimeter
    global birdArea
    global birdPerimeter
    global rhinoArea
    global rhinoPerimeter 
    global cowArea
    global cowPerimeter
    global totalArea
    global totalExternalPerimeter
    global totalFencing
    global cowHeight
    global turtleHeight

    #calculate total area
    totalArea = turtleArea + birdArea + rhinoArea + cowArea
    #calculate total fencing used 
    totalFencing = cowPerimeter + birdPerimeter + rhinoPerimeter + turtlePerimeter
    #calculate total external perimeter
    totalExternalPerimeter = totalFencing - (cowHeight + turtleHeight)


#Displays the area and perimeter of all of the pens-------------------
#---------------------------------------------------------------------
def displayMeasurements():
    #retrieve global variables 
    global turtleArea
    global turtlePerimeter
    global birdArea
    global birdPerimeter
    global rhinoArea
    global rhinoPerimeter 
    global cowArea
    global cowPerimeter
    global totalArea
    global totalExternalPerimeter
    global totalFencing

    #neatly display all areas and perimeters 
    print('The area of the "Moo Cow Pen" is\t\t: {0:>4.0f}'.format(cowArea))
    print('The perimeter of the "Moo Cow Pen" is\t\t: {0:>4.0f}'.format(cowPerimeter))
    print('The area of the "Rhino Common Ground" is\t: {0:>4.0f}'.format(rhinoArea))
    print('The perimeter of the "Rhino Common Ground" is\t: {0:>4.0f}'.format(rhinoPerimeter))
    print('The area of the "Turtle Petting Area" is\t: {0:>4.0f}'.format(turtleArea))
    print('The perimeter of the "Turtle Petting Area" is\t: {0:>4.0f}'.format(turtlePerimeter))
    print('The area of the "Bird Cage" is\t\t\t: {0:>10.5f}'.format(birdArea))
    print('The perimeter of the "Bird Cage" is\t\t: {0:>10.5f}'.format(birdPerimeter))
    print('----------------------------------------------------------------------')
    print('The TOTAL AREA of all regions is\t\t: {0:>10.5f}'.format(totalArea))
    print('The TOTAL LENGTH of external fence is\t\t: {0:>10.5f}'.format(totalExternalPerimeter))
    print('The TOTAL LENGTH of all fence is\t\t: {0:>10.5f}'.format(totalFencing))
    input()

#start main function 
main()