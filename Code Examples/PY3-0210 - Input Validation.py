# Author: Mark Dencler
# Description: This program demonstrates techniques used to validate
#              user input.

def main():
    # TECHNIQUE #1 (PRIMING READS)
    value = eval(input('Please enter a number between 2 and 6: '))
    while value < 2 or value > 6:
        print('That value is not in range... please try again.')
        value = eval(input('Please enter a value between 2 and 6: '))
    print('You indicated a value of: {}'.format(value))
    print('')

    # TECHNIQUE #2 (INITIALIZATION VALUES)
    value_1 = 0
    value_2 = 0
    while (value_1 * value_2) != 100:
        print('Provide numbers who product is 100.')
        value_1 = eval(input('Please enter the first factor : '))
        value_2 = eval(input('Please enter the second factor: '))

        # display error message is re-prompt will occur
        if (value_1 * value_2) != 100:
            print('{} * {} = {}... This is not 100'.format(value_1, value_2,\
                value_1 * value_2))

    print('Ahh... there you go.  {} * {} = {}'.format(value_1, value_2,\
                value_1 * value_2))
          
    print('')
    
        
# Begin MAIN()
main()
