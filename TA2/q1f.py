#
# List sum and Lists comparison program (q1f.py)
#
# Purpose: This program contains two functions to handle and compare lists
# The first function receives a list of numbers and return the sum of all positive numbers in the list or None
# when there is no positive number. This function can help calculate the sum of +ve numbers in a num list.
# 
# The second function compares values in two lists of numbers. If any number in the list parameter 'check' is greater than
# all numbers in the list parameter 'numlist', return True. Otherwise, return False.
# This function is used for list values comparisons.
#
# Limitation: Each function specifies a particular function. You have to re-program the functions to acheive
# list manipulation you want.
# There is no input validation for the list parameters. You cannot ensure that the list elements are numbers without checking
# in reality.
#  
# Written by CHAN CHI HUNG (s12650050)
# On 04/02/2022
# For COMP S258 Assignment 2
#

# sumPos(numList) - Calculate the sum of only the positive numbers
def sumPos(numList):
    # +ve numbers sum count
    sum = 0
    
    # Keep track of status of presence of +ve number in the list
    status = False
    
    # Draw each element in the list
    for num in numList:
        
        # sum when the element is +ve number
        if num > 0:
            sum += num
            
            # presence of +ve number
            status = True
    
    # no +ve number is present, return None
    if not status:
        return None
    
    # return sum of all +ve numbers in the list
    else:
        return sum

# checkLarger(numList, check): Check if any number in the check list is greater than
# all numbers in the numList. Given that check and numList are lists of numbers.            
def checkLarger(numList, check):
    # Keep track of status of presence of a number in check greater than all numbers in numList
    status = False
    
    # Draw each element in the list check   
    for num in check:
        
        # use built-in function max() of list.
        if num > max(numList):
            # Occurence of one case, stop search and return True
            status = True
            break
        
    return status

# define the main function and functions to be demonstrated
# use the skeleton file example
def main():
    print(sumPos([1, 2, 3, 4, 5]))
    print(sumPos([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5]))
    print(sumPos([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 0]))
    print(sumPos([]))
    
    numlist = [1, 9, 6, 3, 4, 6, 2, 4]
    print(checkLarger(numlist, [0, 0, 0]))  # False
    print(checkLarger(numlist, [9, 0, 0]))  # False
    print(checkLarger(numlist, [0, 0, 9]))  # False
    print(checkLarger(numlist, [0, 9, 0]))  # False
    print(checkLarger(numlist, [10, 0, 0]))  # True
    print(checkLarger(numlist, [0, 0, 10]))  # True
    print(checkLarger(numlist, [0, 10, 0]))  # True
    
# execute the main function of the program
main()
           