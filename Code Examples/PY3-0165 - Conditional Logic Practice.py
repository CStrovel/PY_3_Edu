def main(): 
    aaa(True,False,True,True)
    input()
def aaa(bl1, bl2, bl3, bl4):
    #Ask the user about the conditional logic 
    boolQuestion(True, True, False, False, "and", "and", "and")
    #get input from the user 
    answer = True
    #answer = boolInput()
    #test if the user was correct 
    if answer == (bl1 and bl2 and bl3 and bl4):
        print("\nCorrect! Good Job!\n\n") 

#def aao(bl1, bl2, bl3, bl4):

#def aoa(bl1, bl2, bl3, bl4):

#def oaa(bl1, bl2, bl3, bl4):

#def aoo(bl1, bl2, bl3, bl4):

#def ooa(bl1, bl2, bl3, bl4):

#def oao(bl1, bl2, bl3, bl4):

#def ooo(bl1, bl2, bl3, bl4):

# Wrapper for string with replacement fields to avoid having to retype 
# question for every function 
def boolQuestion(bl1, bl2, bl3, bl4, con1, con2, con3):
    #Print the question based on the arguments passed
    print("\nDoes the following conditional statement evaluate to True or False?")
    print("{} {} {} {} {} {} {} :".format(bl1, con1, bl2,
         con2, bl3, con3, bl4), end = "")      

main()