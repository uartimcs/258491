import random

def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)

def quickSortNew(aList, reverse=False, setrand=False):
    quickSortHelper(aList,0,len(aList)-1, reverse, setrand)

def quickSortHelper(aList, first, last, reverse=False, setrand=False):
    pivot_pos = partition(aList, first, last, reverse, setrand)
    quickSortHelper(aList, first, pivot_pos - 1, reverse, setrand)
    quickSortHelper(aList, pivot_pos + 1, last, reverse, setrand)



def partition(aList, first, last, reverse=False, setrand=False):
    
   
    if setrand == True:
     
        set_random = random.randint(first, last)
        
        aList[first], aList[set_random] = aList[set_random], aList[first]
    

    pivot_val = aList[first]
    

    left = first+1
    right = last

    while left <= right:
        
        # no reverse, ascending order
        if reverse == False:
            while left <= right and aList[left] <= pivot_val:
                left += 1
            while right >= left and aList[right] >= pivot_val:
                right -= 1
        
        else:
            while left <= right and aList[left] >= pivot_val:
                left += 1
            while right >= left and aList[right] <= pivot_val:
                right -= 1            
                                
        if left < right:
            aList[left],aList[right] = aList[right],aList[left]


    aList[first],aList[right] = aList[right],aList[first]


    return right
