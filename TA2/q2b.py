#
# Mark-Six numbers selection generating program (q2b.py)
#
# Purpose: A program that allows the user to generate Mark Six numbers (ranges 1 to 49 by enter numbers of entry (K) (where 1<=K<=6) and
# number of balls (N) (where 6<=N<=8) in each entry. The program will generate K entries of N numbers randomly and in a non-repeatable way.
# i.e. Each number appears at most once in all entries.
#
# The program will use the Python built-in random module to select numbers randomly from 1 to 49.
# After that, the selected numbers are removed from the number list and no longer drawn again.
# Since the maximum numbers generated is 8 x 6 = 48. We can ensure each number appears at most once in the entries.
# 
# Limitations: Mark six computer lotteries sold by HKJC usually contain a set of 6-number selection chosen by computer from 1- 49 in a repeatable way.
# This program assume the inputs are integers. but in reality users may input string or combination of string and numbers deliberately or by mistake.
# 
# Written by CHAN CHI HUNG (s12650050)
# On 04/02/2022
# For COMP S258 Assignment 2
#

# import the random module for random numbers and built-in functions
import random

# Create a list of integer from 1 to 49, representing mark six ball set
marksix_set = list(range(1,50))
#print(marksix_set)

# Monitor the selection status of N. Exit the while-loop when completed.
status_N = True

while status_N:
    N = int(input('Enter how many numbers in each entry (N): '))
    
    # The question assumes the input is an integer. Check range only
    if N < 6 or N > 8:
        print('The number in an entry (N) must be between 6 and 8.')
        
    else:
        # Monitor the selection status of K. Exit the while-loop when completed.
        status_K = True
        
        while status_K:
            K = int(input('Enter how many entries (K): '))
            
            # The question assumes the input is an integer. Check range only
            if K < 1 or K > 6:
                print('The number of entries (K) must be between 1 and 6.')
                
            else:
                # Exit the while-loops and ready for printouts.
                status_K = False
                status_N = False

# print the message
print('The {} entries generated:'.format(K))

for i in range(0, K):
    
    # Choose N from the current mark six ball sets
    list_chosen = random.sample(marksix_set, N)
    
    # print one entry
    print(list_chosen)
    
    # The balls are drawn. They cannot be selected again and should be removed from the mark six ball set.
    marksix_set = list(set(marksix_set) - set(list_chosen))
    