#
# QuickSort Comparison program (q2c.py)
#
# Purpose: The program contains an implementation of QuickSort with the function name QuickSort and sorting
# in ascending order. We need to modify a new version of quickSort in part(i) that can sort list of numbers
# in both ascending and descending order by modifying the partition function.
#
# Then we continue to modify the program to create a quickSort function that can make use of randomized pivot strategy in part(ii)
# This strategy make use of random number to determine the pivot position at first for quickSort instead of choosing
# the first item in the list in the original setting.
#
# Finally we make use of the modified functions for performance testing. These functions are used to proceed the same set of data and
# and find out the best one with the lowest processing time on sorting a list of random numbers and a list of reverse sorted ordered numbers.
#
# Limitations: There is no console for the user to input the numbers in the list and the order of sorting.
# This program only compares performance of varied versions of quickSort. For others common sorting algorithms such as 
# merge sort, we have to create the functions separately.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# import the random module for part (ii)
import random

# The original quickSort() Function, without parameter for asc/desc order, without randomisation option
# Just keep it, it still can use, by default it is asc order and no randomization
def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)

# The ultimate modified version of quickSort(), called quickSortNew()
# allow user to determine the order by setting parameter reverse
# allow randomized pivot strategy by setting parameter setrand
# If no specific, default: reverse=False, random=False, same as quickSort(aList)
# part(i)
def quickSortNew(aList, reverse=False, setrand=False):
    quickSortHelper(aList,0,len(aList)-1, reverse, setrand)


# quickSort uses divide and conqueror strategy
# it sorts it by setting the pivot and sort it in two parts
# elements in one side is greater than pivot, another side is smaller than pivot
#  which side depends on parameter reverse
def quickSortHelper(aList, first, last, reverse=False, setrand=False):
    if first < last:
        # deliver the parameter reverse and setrand to partition function
        pivot_pos = partition(aList, first, last, reverse, setrand)
        quickSortHelper(aList, first, pivot_pos - 1, reverse, setrand)
        quickSortHelper(aList, pivot_pos + 1, last, reverse, setrand)


# The core of quickSort
# Modified to deal with randomized pivot strategy, asc/des order
def partition(aList, first, last, reverse=False, setrand=False):
    
    # If setrand is True, uses randomized pivot strategy - part(ii)
    if setrand == True:
        # select a random number between first and last (inclusively)
        set_random = random.randint(first, last)
        # the result may be 0, i.e. the first position as well, but lower chance
        # Ref. to Unit 6 p.72, swap
        aList[first], aList[set_random] = aList[set_random], aList[first]
    
    # Set the pivot value to be element in the first position
    pivot_val = aList[first]
    
    # Set up the running pointers
    left = first+1
    right = last

    while left <= right:
        
        # no reverse, ascending order
        if reverse == False:
            while left <= right and aList[left] <= pivot_val:
                left += 1
            while right >= left and aList[right] >= pivot_val:
                right -= 1
        
        # reverse == True, descending order
        # Swap when the element is greater than pivot value on the left side
        # smaller than pivot value on the right side
        else:
            while left <= right and aList[left] >= pivot_val:
                left += 1
            while right >= left and aList[right] <= pivot_val:
                right -= 1            
                                
        # Swap the two elements to complete the partitioning
        if left < right:
            aList[left],aList[right] = aList[right],aList[left]

    # Put the pivot in the proper position
    aList[first],aList[right] = aList[right],aList[first]

    #return the index position of the pivot value
    return right

# When q2c.py is run as main program, carry out the following part.
# When it is used as module/library, ignore the following part.
if __name__ == '__main__':
    
    # Create a list with 20 elements of integers ranged from 1 to 100 randomly
    aList = []
    for i in range(20):
        aList.append(random.randint(1,100))
        
    # Print the random list    
    print(aList)
    
    # Run the quickSort function for sorting 
    quickSort(aList)
    
    # asc order, with randomization
    #quickSortNew(aList, False, True)
    
    # desc order, without randomization
    #quickSortNew(aList, True, False)
    
    # desc order, with randomization
    #quickSortNew(aList, True, True)
    
    # Print the sorted list after quickSort
    print(aList)
