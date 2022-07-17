#
# Fibonacci numbers generating program (q2b.py)
#
# Purpose: This program consists of two parts.
# In part(i), it allows the user to input the start and end of the Nth Fibonacci number to be shown, then the program will generate
# the Fibonacci number in an ascending order from the start value to the end value using recursive function Fib(N).
#
# The Fibonacci numbers are generated using a given recursive function called Fib(N) and calculate the values recursively.
# However, recursive function are computationally demanding process and the processing time becomes much larger when
# the value of N grows.
# Also, during the calculation, many Fibonacci numbers are repeately calculated, wasting many CPU resources.
#
# In part(ii), We want to find a way to speed up the processing time by storing the results for lower Nth Fibonnacci number
# and when calculating greater Fibonacci number, we can make use of the stored lower Fibonacci numbers.
# Both computational time and CPU resources are reduced. The performance is improved.
# 
# Limitations: There is no validation of the input by the user. We assume that N is a positive integer <= 1000, i.e. integers from 1 to 1000
# We get a faster processing time but we also need extra memory to store the value of previously calculated Fibonacci numbers.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# import the timeit module, I think it is for bench tests
# it is included in the skeleton file...
import timeit

# import lru_cache from functools for part (ii)
from functools import lru_cache

# The original function for Fibonacci numbers in part(i), given
def Fib(N):
    assert N >= 1
    if N == 1 or N == 2:
        return 1
    return Fib(N-1) + Fib(N-2)

# q2b(ii)
# From tutorials, I learnt two methods for speeding up the function
# Method 1 - lru_cache from functools module
# Method 2 - Create a dictionary (as global variable) to hold previous-run 
# Fibonacci numbers
# Since the skeleton contains timeit module, I guess I have to carry out
# benchmark tests for the original function and the accelerated function(s)
# So why not try both of them at the same time :)


# Method 1 - Use lru_cache
# I cannot keep the same name as the original function since I need Fib(N)
# for part(i) and part(ii) comparisons
# Define FastFibCache(N)
@lru_cache(maxsize = 128)
def FastFibCache(N):
    assert N >= 1
    if N == 1 or N == 2:
        return 1
    return FastFibCache(N-1) + FastFibCache(N-2)

# Method 2 - Use a dictionary (key-value pairs)
# I cannot keep the same name as the original function since I need Fib(N)
# for part(i) and part(ii) comparisons
# Define FastFibDict(N)

# Create an empty dict before function
temp_storage = {}

def FastFibDict(N):
    assert N >= 1
    
    # First Check whether the N term of Fibonacci number is presently stored in dict
    if N in temp_storage.keys():
        # return the value at once instead of recursive calculation
        return temp_storage[N]
    
    # Store when N term Fibonacci number is calculated
    if N == 1 or N == 2:
        temp_storage[N] = 1
        return 1
    
    # Store when N term Fibonacci number is calculated
    # return the stored value 
    temp_storage[N] = FastFibDict(N-1) + FastFibDict(N-2)
    return temp_storage[N]
    
# Fib(N), FastFibCache(N) and FastFibDict(N) defined.

# Set the corresponding function RunFib to run each function respectively
# based on set parameter f
def RunFib(A, B, f=0):
    for num in range(A, B+1):
        if f == 0:
            print(num, Fib(num))
        elif f == 1:
            print(num, FastFibCache(num))
        elif f == 2:
            print(num, FastFibDict(num))

   
# Define the stmt and setup used in timeit.timeit()
TEST_SETUP = '''from __main__ import A, B, RunFib'''
TEST_RUN1 = '''RunFib(A, B, 0)'''
TEST_RUN2 = '''RunFib(A, B, 1)'''
TEST_RUN3 = '''RunFib(A, B, 2)'''

# When q2b.py is run as main program, carry out the following part.
# When it is used as module/library, ignore the following part.
if __name__ == '__main__':
    try:
        # Allow user to input the start point and end point of Fibonacci numbers to be shown
        # The question does not specify/assume nature of input A and B, since it is a general requirement for handling error tolerance
        # I added a try-except to handle ValueError
        A = int(input('Enter the start of the series (A): '))
        B = int(input('Enter the end of the series (B): '))
        
        # answer for Q2b part(i)
        # Print the corresponding Fibonacci numbers from A to B
        for num in range(A, B + 1):
            print(num, Fib(num))
            
        # for Q2b part(ii)
        print()
        
        print('Original')
        print(timeit.timeit(stmt=TEST_RUN1, setup=TEST_SETUP, number = 1))
        print()
        
        print('Use lru_cache')
        print(timeit.timeit(stmt=TEST_RUN2, setup=TEST_SETUP, number = 1))
        print()
        
        print('Use dictionary')
        print(timeit.timeit(stmt=TEST_RUN3, setup=TEST_SETUP, number = 1))        
        
    except ValueError:
        print('There is something wrong with the input value(s) ')
    
# Case :  A = 5 and B = 40
# lru_cache (least recently used) may give better performance after multiple trial runs
# demo result (Original) : 95.81483 seconds 
# demo result (lru_cache) : 0.004541 second
# demo result (dictionary) : 0.004035 second