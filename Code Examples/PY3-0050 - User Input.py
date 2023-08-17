# Author: Charles Strovel
# Description: This program demonstates keyboard input.

#python uses the input() function to get data from the keyboard
print("Please enter your name:")     #prompt
result = input()                     #get user input
print("Your name is ", result, "\n") #echo user input 

# input has a built in prompt function
# just pass your prompt string in as an argument 
result = input("Please enter your name: ")    #prompt user and get user input
print("Your name is", result,"\n")            #echo user input 

#input() always gets a string from the keyboard
#if you are expecting a string, use the input() function  
numOne = input("Please enter a number: ")           #get a number from the user
numTwo = input("Please enter another number: ")     #get another number from the user

#notice how the two numbers are concantinated together, not mathmatically added 
print(numOne + numTwo,"\n")                         

#To read in user input as another data type, such as integer or float, 
#pass the input() function to the eval() function 
numOne = eval(input("Please enter a number: "))           #get a number from the user
numTwo = eval(input("Please enter another number: "))     #get another number from the user

#now the numbers are added together before printing! 
print(numOne + numTwo,"\n")       
input()                  