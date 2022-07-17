#
# Mathematical Constant - PI Estimation Program (q2a.py)
#
# Purpose: This program has a recursive function find_pi_square(N) that can approximate the value of square of PI
# using a infinite summation series with an integer N as the parameter.
# The greater the value of N, the closer the value to the square of PI because more terms are added in approximation.
# After that, we can use math.sqrt() to get the PI value we want.(It does not specific in the question but exists in skeleton file)
# 
# Limitations: We assume N is a positive integer <= 500. However, there is no input console and no validation.
# We set the recursion limit to 10000 to our demonstration. Then, stack overflow error occurs if we allow a very 
# large value of N as the parameter. 
# In general, we don't choose a very great value of N because the processing time will be greater with just a little improvement 
# in the approximation of square of PI.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# import math and sys modules
import math, sys

# Set a function find_pi_square with parameter N as a positive integer of <= 500
# i.e. integers from 1 to 500
def find_pi_square(N):
    # assert N >= 1, "There is something wrong with the setting of parameter N"
    
    # Base Case
    # when N = 1, the answer is 8
    if N == 1:
        return 8
    
    else:
        # Return the same function with smaller size of parameter and add the difference value.
        return find_pi_square(N-1) + 8/(2*N-1)**2

# Set number of recursion limit to 10000
sys.setrecursionlimit(10000)

# Set parameter N = 100 to get the approximate value of square of PI using
# the recursive function find_pi_square
pi_square = find_pi_square(100)
#print(pi_square)


# Take the square root of value to get the estimated PI
# it is included in skeleton file
pi = math.sqrt(pi_square)

# Print the estimated PI value to the console
print(f'PI is found to be {pi}')
