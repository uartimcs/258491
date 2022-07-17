#
# degrees,radians,sine and cosine conversion program (q2c.py)
#
# Purpose: This program is to uses a for loop to generate a lookup table for the equivalent radians, sine (Sin) and cosine (Cos) of an angle in degrees.
#
# Limitation: Hard coding, for greater than 90 degrees you need to re-program it.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 06/11/2021
# For COMP S258 Assignment 1 q2c
#

# import math library
import math

# print the 4 columns entities. 10 spaces each column, right alignment.j
print("Degrees".rjust(10), end = "")
print("Radians".rjust(10), end = "")
print("Sin".rjust(10), end = "")
print("Cos".rjust(10))



# For loop, starts from 0 degree, stop at 91 degrees (end at 90 degrees), an increment of 5 degrees
for i in range (0, 91, 5):

# print the 4 columns entities, use repetition operator for 10 spaces    
# degree, radian, sin and cos respectively

    print(format(i,">10.4f"),end = "")
    print(format(math.radians(i),">10.4f"),end = "")
    print(format(math.sin(math.radians(i)),">10.4f"), end = "")
    print(format(math.cos(math.radians(i)),">10.4f"))