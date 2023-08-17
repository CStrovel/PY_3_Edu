# Author: Mark Dencler
# modified for python 3.7 by Charles Strovel
# Description: This program contains a series of exercises dealing with
#              boolean logic and conditional expressions.

def main():
    # SHORT CIRCUIT RULES
    # 1.) If the first boolean expression of an "or" is True
    #     the second boolean expression is not evaluated.
    # 2.) If the first boolean expression of an "and" is False
    #     the second boolean expression is not evaluated.   
    # Determine what value will display as being stored in result
    # after each of the following boolean statements is crunched:
    
    # TEST QUESTION #1
    result = True and False or True and True
    print('1.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #2
    result = False or True or True and False
    print('2.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #3
    result = (False or True or True) and False
    print('3.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #4
    result = not(True and False)
    print('4.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #5
    result = not(not(not(True)))
    print('5.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #6
    x = True
    y = False
    result = True and not(x == y)
    print('6.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #7     (False is less than True
    result = False > True
    print('7.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #8
    result = False < True
    print('8.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #9      (False == False and True == True)
    result = False == False
    print('9.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #10     (False will evaluate to zero)   
    result = False == 0
    print('10.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #11      
    result = False == 1
    print('11.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #12     (True will evaluate to one) 
    result = True == 0      
    print('12.)' , end = "")
    DisplayResult(result)   
    
    # TEST QUESTION #13     
    result = True == 1
    print('13.)' , end = "")
    DisplayResult(result)   
    
     # TEST QUESTION #13     (True does not evaluate to any non-zero)   
    result = True == -1
    print('14.)' , end = "")
    DisplayResult(result)

    input("")
    

def DisplayResult(result):
    print('The value in \'result\' is: {}'.format(result))
    
# Begin MAIN()
main()
