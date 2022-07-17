#
# Scalability Evaluation Program for secret functions (q1a.py)
#
# Purpose: This program evaluates the scalability of three mystery functions, namely
# funcA(), funcB() and funcC() empirically by measuring the time taken to process the same lists with sizes 500,
# 1000, 2000 and 4000 using timeit.timeit() function. 
# The program is executed once to generate the time taken for each function to run the same lists.
# The data generated will be further analyzed to answer some questions, including the scalability.
# 
# Limitations: There is no input console from the user. 
# Instead, the program creates the list by random and copy the same lists for comparison.
# The data size may not be significant to see the difference among functions. The appropriate size should be pre-tested.
# The benchmark test should not spend too much time (Not too long/too short to see the result.)
#
# Written by CHAN CHI HUNG (s12650050)
# On 01/05/2022
# For COMPS258 Assignment 4
#

# import random, timeit and math modules
import random
import timeit
import math

# The first mystery function, funcA()
def funcA(numlist):
    for i in range(len(numlist)):
        index = i
        for j in range(len(numlist)):
            if numlist[index] > numlist[j]:
                numlist[j], numlist[index] = numlist[index], numlist[j]
            k = math.factorial(500)
            
# The second mystery function, funcB()
def funcB(numlist):
    total = 0
    for i in range(1000):
        for j in range(100):
            total += i**j
            
# The third mystery function, funcC()
def funcC(numlist):
    count, k = 0, 0
    for i in range(len(numlist)):
        j = i
        while j > 0:
            if numlist[i] + numlist[j] == k:
                count += 1
            k = i ** j
            k += math.factorial(500)
            j = j // 2


if __name__ == '__main__':
    
    # Set up the import function and list used in comparison
    SETUP_ENVA = '''from __main__ import funcA, aList'''
    SETUP_ENVB = '''from __main__ import funcB, bList'''
    SETUP_ENVC = '''from __main__ import funcC, cList'''

    # The running code in the performance evaluation of each function
    TEST_FUNCA = '''funcA(aList)'''
    TEST_FUNCB = '''funcB(bList)'''
    TEST_FUNCC = '''funcC(cList)'''

    # Data size required: 500, 1000, 2000, 4000
    for size in (500, 1000, 2000, 4000):
        # Create an empty list to hold the set of data
        aList = []
        
        # Append appropriate number of data to the list.
        # The question does not specify the data to be used. So I follow the study note
        for num in range(size):
            aList.append(random.uniform(1, 10000))

        # Copy two set of lists for fair comparison.
        bList = aList.copy()
        cList = aList.copy()            
        
        # Performance evaluation for each function and get the results.
        resultA = timeit.timeit(setup=SETUP_ENVA, stmt = TEST_FUNCA, number = 1)
        resultB = timeit.timeit(setup=SETUP_ENVB, stmt = TEST_FUNCB, number = 1)    
        resultC = timeit.timeit(setup=SETUP_ENVC, stmt = TEST_FUNCC, number = 1)
        
        # Output the results
        # The reported time is expressed as second(s) in 4 decimal places.
        print("List Size:", size)
        print("funcA - Time taken : {:.4f} s".format(resultA))
        print("funcB - Time taken : {:.4f} s".format(resultB))    
        print("funcC - Time taken : {:.4f} s".format(resultC))
        print()        
 
 