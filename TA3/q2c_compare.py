#
# QuickSort Comparison program (q2c_compare.py)
#
# Purpose: The program contains an implementation of QuickSort with the function name QuickSort and sorting
# in ascending order. We need to modify a new version of quickSort in part(i) that can sort list of numbers
# in both ascending and descending order by modifying the partition function.
#
# Then we continue to modify the program to create a quickSort function that can make use of randomized pivot strategy in part(ii)
# This strategy make use of random number to determine the pivot position at first for quickSort instead of choosing
# the first item in the list in the original setting.
#
# Finally we make use of the modified functions for performance testing (q2c_compare.py). These functions are used to proceed the same set of data and
# and find out the best one with the lowest processing time on sorting a list of random numbers and a list of reverse sorted ordered numbers.
#
# Limitations: There is no console for the user to input the numbers in the list and the order of sorting.
# This program only compares performance of varied versions of quickSort. For others common sorting algorithms such as 
# merge sort, we have to create the functions separately.
#
#
import random
import timeit

# import necessary components for performance testing
# We will use quickSortNew function in q2c.py and aList, bList created in the main program (i.e. q2c_compare.py)
SETUP_QUICKSORT = '''
from q2c import quickSortNew
from __main__ import aList, bList'''

# quickSortNew with default parameters - original setting:
# same as quickSort(aList)

# asc order, no randomized pivot strategy      
TEST_QUICKSORT = '''quickSortNew(aList)'''

# quickSortNew with setrand parameter = True - asc order, randomized pivot strategy applied
TEST_QUICKSORTR = '''quickSortNew(bList,setrand=True)'''

# Test on random list of floating point numbers with 4 different data sizes
# of random floating numbers ranging from 0 to 10000
for N in (100,200,400,800): 
    
    # Set a list to hold N floating point numbers
    aList = []
    # GENERATE A RANDOM LIST OF N floating point numbers (range 0 to 10000) in aList
    for num in range(N):
        aList.append(random.uniform(0, 10000))
        
    # Make a copy of list to the competitor
    bList = aList.copy()
    
    # Print the results to the console
    print("Randomly ordered")
    print("Size: ", len(aList))
    print("quickSort - {:.5f} second(s)".format(timeit.timeit(setup = SETUP_QUICKSORT, stmt = TEST_QUICKSORT, number = 1)))
    print("Randomized quickSort - {:.5f} second(s)".format(timeit.timeit(setup = SETUP_QUICKSORT, stmt = TEST_QUICKSORTR, number = 1)))
    print()

# Test on  list of floating point numbers with reversely sorted ordered
# Test with four data size of random floating numbers ranging from 0 to 10000    
for i in (100,200,400,800):

    # Set a list to hold N floating point numbers
    aList = []
    # GENERATE A LIST OF reversed sorted i floating point numbers (range 0 to 10000) in aList
    for j in range(i):
        aList.append(random.uniform(0, 10000))
    # Create a reverse sorted ordered sequence to test
    aList.sort(reverse=True)
    #print(aList)
    # Make a copy of list to the competitor
    bList = aList.copy() 
    
    # Print the results to the console
    # The list has been reversely ordered, and we sorted them to ascending order with and without randomized pivot strategy.
    print("Reverse sorted ordered")
    print("Size: ", len(aList))
    print("quickSort - {:.5f} second(s)".format(timeit.timeit(setup = SETUP_QUICKSORT, stmt = TEST_QUICKSORT, number = 1)))
    print("Randomized quickSort - {:.5f} second(s)".format(timeit.timeit(setup = SETUP_QUICKSORT, stmt = TEST_QUICKSORTR, number = 1)))
    print()