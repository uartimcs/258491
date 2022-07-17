#
# Count program for an equation (q3a.py)
#
# Purpose: This program is to find out how many combinations (a, b, c) that make the equation correct. 
#
# Limitation: The value of a, b and c are hard coded. You need to change program code for different ranges of values
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q3a
#

# Set the counter and initialize the value 0.
# count number of matches
counter= 0

# outer loop , iterate c from 1 to 1000
for c in range (1, 1001):
    
    # nested loop
    # to iterate a from 1 to 1000 for each c
    for a in range (1, 1001):
        
        # nested loop
        # to iterate b from 1 to 1000 for each a
        for b in range (1, 1001):
            
            if (c**3 == a**2 + b**2):
                # counter + 1 when one match is found
                counter += 1
                
                # since c is of cubic, it increases faster than square as numbers become larger.
                # break the loop when c^3 is greater than max value of a^2 + b^2 to save time and CPU resources
            if (c**3 > 1000**2 + 1000**2):
                break

# show the total combinations
print("The number of combinations =",counter)
    


