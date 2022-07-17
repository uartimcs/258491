#
# Square Printing Program - Version B (q1b.py)
#
# Purpose: This program prints a square of default pattern with arbitary size (>0) based on user input.
# The square consists of a descending number of '$' sign (from row size to 1)  
# and the reminder by 10 of ascending number starting from row size.
# This program can validate the user input to ensure the user input is of integer type and greater than zero. 
#
#
# Limitation: This program can print square only, i.e. with the same row and column size. Not for rectangle or trapezium.
# The square consists of '$' and numbers only. The user cannot specific the symbols/numbers he/she wants.
# This program does not allow the user to re-enter the data when the input validation fails.  
# 
# Written by CHAN CHI HUNG (s12650050)
# On 03/02/2022
# For COMP S258 Assignment 2
#

# input validation for integer type
try:
    # allow the user to input the size of square.
    size = int(input('Enter size of pattern: '))
    
    # A square must have width > 0.
    if size <= 0:
        print('The number must be a positive integer')
        
    else:
        # the outer for-loop controls the rows. row size = input size 
        for i in range (0, size):
            
            # the inner for-loop(s) control the column.
            
            # this for-loop controls the '$' sign printed in descending number down the row.
            for j in range (i, size):
                print('$', end='')
            
            # this for-loop controls the numbers printed down the row.
            # Reset the count variable to the input size.
            count = size
            for k in range (0, i):
                # The input value itself, or the new value of count during the loop may be greater than 10.
                # Modulo operation to get the value [0 - 9]
                count = count % 10
                print(count, end='')
                
                # count value + 1 after each row printed.
                count += 1
                
            # complete a column pattern and give a line break.
            print('')
    
except ValueError:
    # catch the exception of ValueError and print message to notify the user
    print('The input must be an integer')
