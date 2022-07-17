#
# Square pattern printing program (q2d.py)
#
# Purpose: This program is use to generate a square pattern based on user input.
#
# Limitation: Limited to values ranged from 1 to 20 only.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 06/11/2021
# For COMP S258 Assignment 1 q2d
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
            print("+"*(size-2),end="")
                
            # end with a closing $ sign in each row   
            print("$")
            
        # row end
        
        # complete work, counter + 1
        counter += 1
        
# invalid input and show error msg        
else:
    print("The entered size should fall between 1 to 20")
