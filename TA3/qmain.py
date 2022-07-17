import random
import quickSort

numlist = []
for i in range(0, 10):
    result = random.randint(0, 1000000)
    numlist.append(result)

# The quickSort function sorts the original list, no return list
print(numlist)
quickSort.quickSort(numlist)
print(numlist)



#aList = []
#for i in range(0, 10):
   # result = random.randint(0, 1000000)
    #aList.append(result)
#quickSort.quickSort(aList)
#numlist += aList
#print(numlist)
    