#Author: Charles Strovel
#Discription: This program is an alternate version of PY3_A02S00, demonstrating function reusability  
#this assignment is to teach students prompt formatting and appropriate use of functions.
 
#main function, retreaves data from user------------------------------
#then calls functions to do the math and display---------------------
def main():
    #get length and height of cow pen from user
    cowHeight = eval(input("Please enter moo-cow pen height\t\t: "))
    cowLength = eval(input("Please enter moo-cow pen length\t\t: "))
    #calculate cow area and cow perimeter
    cowArea = area(cowHeight, cowLength)
    cowPerimeter = perimeter(cowHeight, cowLength)

    #get length and height of rhino common ground from user
    rhinoHeight = eval(input("Please enter rhino common ground height\t: "))
    rhinoLength = eval(input("Please enter rhino common ground length\t: "))
    #Calculate rhino common ground perimeter and area
    rhinoArea = area(length = rhinoLength, width = rhinoHeight)
    rhinoPerimeter  = perimeter(length = rhinoLength, width = rhinoHeight)

    #get length and height of turtle petting area from user
    turtleHeight = eval(input("Please enter turtle petting area height\t: "))
    turtleLength = eval(input("Please enter turtle petting area length\t: "))

    #calculate turtle petting area perimeter and area
    #using a combination of kwargs and positional args
    turtleArea = area(turtleLength, width = turtleHeight)
    turtlePerimeter = perimeter(turtleLength, width = turtleHeight)

    #get radius of the bird cage from user
    radius = eval(input("Please enter radius of the bird cage\t: "))
    #clculate area and perimeter of the bird cage 
    birdPerimeter = circumference(radius)
    birdArea = circArea(radius)
    
    #calculate total area and perimeters 
    #assigned to vars for readability 
    totalArea = total(cowArea, rhinoArea, turtleArea, birdArea)
    totalFencing = total(cowPerimeter, rhinoPerimeter, turtlePerimeter, birdPerimeter)
    totalExternalPerimeter = totalFencing - (cowHeight + turtleHeight)

    #display measurements in a pleasing way
    displayMeasurements(cowArea, cowPerimeter, rhinoArea, rhinoPerimeter, turtleArea, turtlePerimeter,
    birdArea, birdPerimeter, totalArea, totalFencing, totalExternalPerimeter)
    
#Calculates square area given length and height-----------------------
#--------------------------------------------------------------------
def area(length, width):
    return length * width

#Calculates perimeter distance given length and height-----------------
#---------------------------------------------------------------------
def perimeter(length, width):
    return length * 2 + width * 2

#calculates the perimiter of a circle----------------------------------
#---------------------------------------------------------------------
def circumference(rad):
    #set PI
    PI = 3.14159

    #calculate and populate
    return  2 * PI * rad

#calculates the area of a circle---------------------------------------
#---------------------------------------------------------------------
def circArea(rad):
    #set PI
    PI = 3.14159

    return PI * rad ** 2 

#calculates sum of args passed-----------------------------------------
#---------------------------------------------------------------------
def total(var1, var2, var3, var4):
    #calculate total
    return var1 + var2 + var3 + var4

#Displays the area and perimeter of all of the pens-------------------
#--------------------------------------------------------------------
def displayMeasurements(cowArea, cowPerimeter, rhinoArea, rhinoPerimeter, turtleArea, turtlePerimeter,
    birdArea, birdPerimeter, totalArea, totalFencing, totalExternalPerimeter):
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