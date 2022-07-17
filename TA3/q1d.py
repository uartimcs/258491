#
# Best Soccer Team Analysis Program (q1d.py)
#
# Purpose: This program can analyze and print the finding of the best Soccer Team and the corresponding Win-Rate
# through reading a csv file (EPLTeams.csv) containing the number of games played and the number of winning 
# games for some soccer teams.  
# If there are two or more teams with the same highest, choose any.
#
# The program should print the findings to the screen on a single line, and then print 'Analysis finished' 
# on the next line before the end of execution. 
# The program has no input from user and print 'IO Error' if there is an error in file operations.
#
# Limitations: The csv file format must follow the format of EPLTeams.csv and the file name must be the same
# or otherwise the file cannot be read and IOError is resulted in.
# The csv file should be of the same folder as the program. There is no input from the user. 
# The data rely on the csv file. You cannot change the column order of the .csv file because the data
# is searched by column no. instead of name of column.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# import the sys module and random module
import sys
import random

# csv file to be opened. Use a variable to hold it instead of hard-coding
# same folder as the program
file_name = 'EPLTeams.csv'

# Best Soccer Team name and its win-rate
best_name = None
best_rate = None                
            
# Counter/Pointer of line read
count_line = 0    

#try-except to handle exceptions
try:
    # Open the csv file, read only
    # if failed, catch IOError/OSError exceptions
    file = open(file_name, 'r')
    
    while True:
        
        # Read the csv data line-by-line
        # Line pointer + 1
        result_line = file.readline()
        count_line += 1
        
        # When the result_line is empty str, file read is complete and exit while loop
        if result_line == '':
            break
        
        # the data line may contain leading/trailing spaces and '\n' line feed - handled with strip() and rstrip()
        # The data in three columns are separated by comma in .csv file - handled with split(',')
        # Get the data in the form of list with indexing as columns, from 0 to 2 (there are three columns)
        data = result_line.strip().rstrip().split(',')
        
        # The first row is the topic header, ignored
        if count_line == 1:
            continue
        
        # When read the second row
        # Initialize variables best_name and best_rate with data in row 2
        # The best_name and best_rate will be replaced when reading a team
        # with better win-rate down the rows.
        elif count_line == 2:
            best_name = data[0]
            # rate = number of winning games divided by number of games played in %
            best_rate = 100 * int(data[2])/int(data[1])
            
        # Other lines - get the values for comparison
        else:
            team_name = data[0]
            team_rate = 100 * int(data[2])/int(data[1])
            
            # When the team_rate is greater the best_rate, assign with new values
            if team_rate > best_rate:
                best_name = team_name
                best_rate = team_rate
            
            
            # The chance of exactly equal rate is considerably low.
            # This part is just for fun. The question states if they have the same rate, choose any
            # generate random number, if it is equal to 1, replace it with the incoming one or just keep it when it is 0.
            elif team_rate == best_rate:
                random_no = random.randint(0, 1)
                
                # Choose the team when the random number is 1.
                if random_no == 1:
                    best_name = team_name
                    best_rate = team_rate
                    
    # close the file after use
    # If use "with open", this step can be skipped.      
    file.close()
    
    # Print the result to the console after analysis in one line
    # Percentage expressed in 4 decimal places
    print('The best soccer team is {} and the winning percentage is {:.4f}%'.format(best_name, best_rate))
    print('Analysis finished')
    
# When there is an error in file operations, print IOError
# From stackoverflow - IOError merged into OSError in Python 3.3
# For playsafe I catch exception in this way instead of except IOError:        
except (OSError,IOError):  

    # The skeleton file import sys, I think i can use it here.
    sys.stderr.write('IOError')


# It is not required in the question, but added according to tutor's recommendations
# catch other possible error(s) encountered and show error message to the console
except:
    sys.stderr.write('Error')
    


