#
# Conference Room Distribution Program (q3a.py)
#
# Purpose: This program can schedules the meetings in a conference room (“A”) such that as
# many meetings as possible can be held on a given day. Any meetings that cannot be held in 
# conference room A can be moved to another conference room (“B”) if it is unoccupied during 
# the requested period, otherwise the meeting is rejected.
# The meeting requests are stored in a CSV file meeting_requests.csv
# 
# Limitations: The file name must be meeting_requests.csv. If there is any change in the filename
# and the layout of the csv file. The program has to be rearranged.
# This file should follow the united data format in each fields of the csv files.
#
# Written by CHAN CHI HUNG (s12650050)
# On 02/05/2022
# For COMPS258 Assignment 4
#
#import csv # I prefer not to use csv.reader
import datetime
import sys

# Load the set of requests from csv file and store in the list
# I will sort them in terms of ascending endTime
booking_requests = []

# Register the timeslots occupied
conferenceA = []
conferenceB = []

# Register request numbers' distribution results
# i.e. allocate conference room A, B or rejected
requestA = []
requestB = []
rejectedRequest = []

# Program Descriptions
# Two functions are set first : readBooking() and readConferenceB()
# read and load data in csv file to the list booking_requests and conferenceB
# Not specific in question, but I put the invalid order to rejectedRequest, e.g. outside 8 AM to 7PM
# startTime > endTime (wrong filling)

# readBooking()
# Read the csv file and distribute the requests to booking list or rejected list
# Sort the book list by end time for assignment for easier comparison
def readBooking(file_name):
    
    # Pointer for navigation of row read
    row_pointer = 0
    try:
        # Open the file or catch IOError
        file = open(file_name, 'r', encoding="utf-8-sig")
        
        # Read the file line-by-line until it is empty
        while True:
            result = file.readline()
            row_pointer += 1
            
            if result == '':
                break
            
            # The first line is the header, ignored
            if row_pointer == 1:
                continue
            
            else:
                # Create an temp empty list 
                # Hold each timeslot requests
                temp = []
                
                # Split line with comma and form a list of data
                data = result.rstrip('\n').strip().split(",")
                
                # For time comparison, convert startTime and endTime into number of seconds pass since 12:00 AM
                data[1] = datetime.datetime.strptime(data[1], "%I:%M %p")
                startTime = data[1].hour * 60 + data[1].minute
                data[2] = datetime.datetime.strptime(data[2], "%I:%M %p")
                endTime = data[2].hour * 60 + data[2].minute
                              
                # if the timeslot is not appropriate, place it in rejected list. 8 AM - 7 PM
                if (startTime < 8 * 60 or startTime > 19 * 60) or (endTime < 8 * 60 or endTime > 19 * 60):
                    rejectedRequest.append(data[0])
                    
                # inappropriate setting, kick out
                elif startTime > endTime:
                    rejectedRequest.append(data[0])
                                   
                # add to the booking list
                else:
                    temp.append(data[0])
                    temp.append(startTime)
                    temp.append(endTime)
                    
                    booking_requests.append(temp)
        
        # sort the booking requests by ascending endTime for best arrangement
        # greedy algorithm is used.                           
        file.close()
        booking_requests.sort(key=lambda x: x[2])    
        #print(booking_requests)        
    except (OSError, IOError):
        print('Cannot open the file', file_name)
        sys.exit(1)


# readConferenceB
# There are several occupied timeslots in Conference Room B
# Add those timeslots in the ConferenceB first, assume no timeslot crash
def readConferenceB(file_name):
    # Pointer for navigation of row read
    pointer = 0
    try:
        # Open the file or catch IOError
        file_read = open(file_name, 'r', encoding="utf-8-sig")

        # Read the file line-by-line until it is empty
        while True:
            result = file_read.readline()
            pointer += 1

            if result == '':
                break
            
            # The first line is the header, ignored
            if pointer == 1:
                continue
            else:
                
                # Data conversion of startTime and endTime in seconds
                data = result.rstrip('\n').strip().split(",")
                
                data[0] = datetime.datetime.strptime(data[0], "%I:%M %p")
                startTime = data[0].hour * 60 + data[0].minute
                data[1] = datetime.datetime.strptime(data[1], "%I:%M %p")
                endTime = data[1].hour * 60 + data[1].minute
                
                # append startTime and endTime in the list
                conferenceB.append(startTime)
                conferenceB.append(endTime)
                
        file_read.close()
        # The question did not specify whether data in conf_B_sched.csv is in ascending order
        # sorted the whole list for better comparison
        conferenceB.sort()
        #print(conferenceB)
    except (OSError, IOError):
        print('Cannot open the file', file_name)
        sys.exit(1)

# Define a function checkSlot to check availability
def checkSlot(start, end, aList):
    # if the list is empty, of course okay    
    if len(aList) == 0:
        return True
    else:
        # check the min value and max value of a sorted list
        # sort it every addition or requests are added in order
        min_value = min(aList)
        max_value = max(aList)
        
        # I check the validity when adding request number
        # It is within the range 8AM - 7PM already
        if end <= min_value or start >= max_value:
            return True
        else:
            # timeslot in partitions, check whether I can insert a new
            # timeslot between partitions
            for i in range(0, len(aList)):
                if i % 2 != 0 and i != len(aList) - 1:
                    if start >= aList[i] and end <= aList[i+1]:
                        return True
    return False

# Load the data to the lists     
readBooking("meeting_requests.csv")         
readConferenceB("conf_B_sched.csv")     
#print(booking_requests)
#print(conferenceB)

for num in booking_requests:
    # empty conference A booking, just add is okay
    if len(conferenceA) == 0:
        # add the request number to conferenceA
        requestA.append(num[0])
        
        # Occupy the timeslots of the room
        conferenceA.append(num[1])
        conferenceA.append(num[2])
        
    else:
        # non-zero, occupied
        # Check availability of the request in conference Room A and B in desired timeslot
        resultA = checkSlot(num[1], num[2], conferenceA)
        resultB = checkSlot(num[1], num[2], conferenceB)
        
        # Okay, the priority to add conference A first
        if resultA:
            requestA.append(num[0])
            conferenceA.append(num[1])
            conferenceA.append(num[2])
            
            # My algorithm is weak in this part because I have to sort it in each addition
            # In theory there is no need to sort because they are arranged by endTime already
            conferenceA.sort()
        
        # Room A is not okay, try Conference Room B
        # if B is okay, add the timeslots and request number
        elif resultB:
            requestB.append(num[0])
            conferenceB.append(num[1])
            conferenceB.append(num[2])
            
            conferenceB.sort()
        # Both are not okay, request numbers in rejected list.    
        else:
            rejectedRequest.append(num[0])                 

# Output the results to the console
print('Conference A Schedule:', end = " ")
for i in range(0, len(requestA)):
    if i != len(requestA)-1:
        print(requestA[i], end=",")
    else:
        print(requestA[i],end="")
print()    

print('Conference B Schedule:', end = " ")
for j in range(0, len(requestB)):
    if j != len(requestB)-1:
        print(requestB[j], end=",")
    else:
        print(requestB[j],end="")
print()   
 
print('Rejected Meetings:', end=" ")
for k in range(0, len(rejectedRequest)):
    if k != len(rejectedRequest)-1:
        print(rejectedRequest[k], end=",")
    else:
        print(rejectedRequest[k],end="") 