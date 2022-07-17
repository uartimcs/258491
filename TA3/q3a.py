# Files Listing program (q3a.py)
#
# Purpose: This program can print out the list of files in the current directory, along with 
# their file sizes and last modified datetime stamps. Sub-directories are ignored.
# At the end, it prints the total file size.
# The user can sort the list of files to be displayed by adding command line arguments in cmd on Windows
# or terminal on Mac. Available sorting methods include by name, by size and by date and the order can be
# in ascending order or descending order. By default it is sorted by ascending order of name.
#
# Limitations: There is no console for the user to input. Instead, the user have to input the
# command line arguments using cmd on Windows or terminal on Mac
# e.g. python q3a.py date desc
# The sub-directories and their files are ignored in the result printed.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# import the necessary modules to list files in the directory
import os
import sys
import time

# Since I use lambda expression, I don't need the following module provided in skeleton file
#from operator import itemgetter, methodcaller


# Basic variables for file listing purposes
# path - current directory, fileList - store info of files
path = '.'
fileList = []

# Function to get the file listed for the current directory and sorting
# according to default value or user-specific requirements
def showDirectory(path, sort_field, sort_order):
    
    # default values - sort by asc name
    order_desc = False
    sort_code = 0
    
    # user-specific req checks
    # change the default values when appropriate or just neglected
    
    # sort parameter
    if sort_field == 'size':
        sort_code = 1
    elif sort_field == 'date':
        sort_code = 2
        
    # sort order
    if sort_order == 'desc':
        order_desc = True
    
    # Get the file listing for the current directory
    with os.scandir(path) as it:
        # Set a counter to count the total size of files
        entry_count = 0
        for entry in it:
            # print(type(entry))
            # only cares when it is a file
            if entry.is_file():
                # Set a list for holding a file info
                file_collection = []
                file_name = os.path.basename(entry)
                
                file_collection.append(file_name)
                # In Mac/Linux, it will show all hidden files started with ., e.g. .access
                # I want to neglect them because they sort them separately on Mac.
                # I assume it works on cmd, Windows only, so I don't handle it
                #if not file_name.startswith('.'):
                    # tore the name of file
                    #file_collection.append(file_name)
                #else:
                    #continue
                
                # Get the size of a file
                size = os.path.getsize(entry)
                # add the size to counter
                entry_count += size
                # Store the size of file
                file_collection.append(size)
                
                # Store the formatted last modified date
                file_collection.append(os.path.getmtime(entry))
                
                # Add the file info to the collection list
                fileList.append(file_collection)
         
        # Using lambda function for sorting based on requirements
    fileList.sort(key=lambda x: x[sort_code], reverse=order_desc)
        
    print('Filename', 'Size', 'Last Modified')
    for i in fileList:
        print(i[0],'/ ',i[1],'/ ',time.ctime(i[2]))
            
    print('Total file size:', entry_count)

    

# HANDLE THE INPUT ARGUEMNTS

# More than three arguments, not acceptable
# Print usage message and exit the program
if len(sys.argv)  > 3:
    print("Maximum of 2 arguments expected: python fileSorter.py [sort field] [sort order]")
    sys.exit(1)
# COMPELTE THE REMAINING PART OF INPUT ARGUMENT HANDLING

# sys.argv[0] stores the filename - q3a.py
# The size of array is at least one
# When no argument or argument not included, then use default values
# Replace the default value when user has specific valid parameter(s) provided.

# default values of sorting by and the order
sort_field = 'name'
sort_order = 'asc'


# two arguments, len(sys.argv) == 3
if len(sys.argv) == 3:
    
    # Replace with user-specific value when appropriate
    if ((sys.argv[1] == 'name') or (sys.argv[1] == 'size') or (sys.argv[1] == 'date')):
        sort_field = sys.argv[1]
    
    if ((sys.argv[2] == 'desc') or (sys.argv[2] == 'asc')):
        sort_order = sys.argv[2]

# one arguments, len(sys.argv) == 2, default sort order is asc
elif len(sys.argv) == 2:
    if ((sys.argv[1] == 'name') or (sys.argv[1] == 'size') or (sys.argv[1] == 'date')):
        sort_field = sys.argv[1]    


# COMPLETE THE REST OF THE PROGRAM
showDirectory(path, sort_field, sort_order)



