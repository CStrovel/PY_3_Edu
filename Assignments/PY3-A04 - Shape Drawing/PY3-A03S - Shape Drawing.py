# Written by: Charles Strovel
# Python 3.7 Shape Drawing sample code
# Each function uses a different way to draw these shapes
# Any of the methods can be adapted to drawing any of the shapes
def main():
    drawRect(15,10)
    drawTri(8)
    drawPyramid(7)
    input()

#Function to draw a rectangle---------------------------------------
#This function uses for loops---------------------------------------
def drawRect(length, height):
    # for this function we will be compsing the shape in a string
    # and then displaying it
    rectString = ""

    # This function must use for loops, and requires two loops to 
    # accomplish the task. First loop draws height and line breaks 
    for i in range(height):

        # second loop draws horizontal rows 
        for i in range(length):
            rectString += "* "

        # shift to a new line after the nested loop is finished drawing a line
        rectString += "\n"

    #Display the rectangle 
    print("Displaying a {0} x {1} rectangle.\n".format(length, height))
    print(rectString)

# Function to draw a right triangle----------------------------------
# This function uses while loops-------------------------------------
def drawTri(height):
    # define variables. While loops do not automatically provide an index
    # start the index at one, otherwise the first line will print nothing 
    i = 1 

    print("Displaying a triangle of height %d." % height)
    print("")
    
    # for this function we will be printing output directly
    while i <= height:
      # print i asterisks on this line 
      print("* " * i)

      # incriment the loop index 
      i += 1 

# Function to draw a pyramid based-----------------------------------
# on a user defined radius-------------------------------------------
def drawPyramid(rad):
    #declare index
    x = 0

    print("\nDisplaying a pyramid with a base radius of %d.\n" % rad)
    #verticle control loop 
    while x <= rad:
    
        #loop to create left justified padding
        for i in range(rad - x):
            print(" ", end = " ")

        #loop to create asterisk line. Two for each line after the first.
        for i in range(x * 2):
            print("*", end = " ")
        
        #one extra for the centerline column and new line
        print("*")

        #incriment loop
        x += 1 

main()