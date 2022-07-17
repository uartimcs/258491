#
# Square pattern printing program (different pattern) (q2e.py)
#
# Purpose: This program is use to generate a square pattern based on user input.
#
# Limitation: Limited to values ranged from 1 to 20 only.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q2e
#

# Give an input instruction to the user and allow the user to input the size of square printed.
size = int(input("Enter the size of the pattern: "))

# size 1 - 20 
if size >= 1 and size <= 20:
    # set counter to count loop
    counter = 1
    
    #while loop from 1 to number of size
    while counter <= size:
        
        # row setting
        
        # $ is a must to be printed in every row
        print("$", end ="")
        
        # end for size = 1. if size >=2, carry on to form the rest shape.
        if size >= 2:
            
            # Run a for loop from 1 to (size-2) to print number.
            for i in range (1, (size-2) + 1):
                
                # find the quotient [0-9] to print. Start showing number for size = 3
                number_shown = i % 10
                print(number_shown, end="")
                
            # end with a closing $ sign in each row   
            print("$")
            
        # row end
        
        # complete work, counter + 1
        counter += 1
        
# invalid input and show error msg        
else:
    print("The entered size should fall between 1 to 20")
