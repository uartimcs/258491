#
# England toplevel League Soccer Teams Analysis Summary Program (q1c.py)
#
# Purpose: This program can read in data from the csv file about soccer teams in England top level league
# and then prints out the following findings.
# - The name and the points of top 5 teams with the highest points.
# - The number of teams with name containing "United" and won fewer than 500 games.
# - The number of teams that have played over 2000 games and scored over 5000 goals.
# The csv file contains all necessary data for the data analysis. The original name is EnglishLeagueAllTime.csv
# and the program allows the user to input the specific name of the csv file for analysis.
#
# Limitations: This program uses the pre-defined format of csv file for data fetching and analysis.
# When there is a change in the column arrangement, the program needs to be amended. 
# This question assumes that the format of the lines of data is correct.
#
# Written by CHAN CHI HUNG (s12650050)
# On 01/05/2022
# For COMPS258 Assignment 4
#
# import the sys module for error printout
import sys

# Pre-define some variables for data I/O and data collection.
# The number of lines fetched in csv file.
row_pointer = 0
# Hold the name and point of each team for later analysis.
team_point = []
# count the number of teams with name = United and won fewer than 500 games.
name_target = 0
# count the number of teams that have played over 2000 games and scored over 5000 goals.
game_target = 0


# allow the user to input the name of csv file for data analysis
fname = input('Enter CSV filename (Enter to quit): ')
# tested fname = 'EnglishLeagueAllTime.csv'
    
# User presses Enter to quit
if len(fname) == 0:
    sys.exit()

#try-except to handle exceptions
try:
    # Open the csv file, read only
    # if failed, catch IOError/OSError exceptions
    file = open(fname, 'r')
    
    while True:
        # Read the csv data line-by-line
        # pointer + 1
        result_line = file.readline()
        row_pointer += 1
        
        # file read completed, exit the while loop
        # Show the result
        if result_line == '':
            break
        
        # The first line is the header, ignored
        if row_pointer == 1:
            continue
        
        # Remove line feeder and spacing, split by comma
        data = result_line.rstrip().strip().split(",")
        
        # First Task: Add the data for generation of top five
        # Create a temporary empty list to hold the team name and points
        temp = []
        
        # The first column refers to the team name
        temp.append(data[0])
        # The last column refers to the team points, convert to int type
        temp.append(int(data[8]))
        
        # append the [team name, team point] set to team_point list
        # for centralize the sorting and generate five top teams
        team_point.append(temp)
        
        # Second Task: Count the number of teams with name containing "United"
        # and won fewer than 500 games
        
        # The first column refers to the team name and the third column refers to win games
        # add one to name_target when matched.
        if "United" in data[0] and int(data[2]) < 500:
            name_target += 1
            
        # Third Task: Count the number of teams that have played over 2000 games
        # and scored over 5000 goals.
        
        # The second column refer to number of plays and the nummber of scores(For)
        # add one to game_target when matched.
        if int(data[1]) > 2000 and int(data[5]) > 5000:
            game_target += 1
            
    # Complete the operation
    # 1 - file close
    file.close()
    
    # Print the summary to the console
    # Sort the list by points and list from the greatest to smallest
    team_point.sort(key = lambda x: x[1], reverse = True)
    
    # Show the top five summary results:
    for i in range(5):
        print("Team name:", team_point[i][0], "Points:", team_point[i][1])
                
    # Show the number of results for specified conditions.
    print()
    print('The number of teams with name containing "United" and won fewer than 500 games: ', name_target)
    print('The number of teams that have played over 2000 games and scored over 5000 goals: ', game_target)

    
except (OSError, IOError):
    print('IOError:', 'Problem exists when reading the file', fname)