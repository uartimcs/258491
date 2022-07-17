#
# Print out the rating on user-defined hotel (q1c.py)
#
# Purpose: This program is to print the rating (0-10) to an input hotel.
#
# Limitation: There is no error checking (e.g. marks > 10) for the user's input. 
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 06/11/2021
# For COMP S258 Assignment 1 q1c
#

# Open message
print("Rate a Hotel System")

# Give an input instruction to the user and allow the user to input the name in the console.  
hotel_name = input("Enter hotel name: ")

# Give an input instruction to the user and allow the user to input the score in the console.
# data type is string , convert it to float type using float()
score = float(input("Enter score (0-10) for the hotel: "))

# Output the score to input hotel, score rounding to 1 decimal place.
print("Thank you for given {:.1f} to {}".format(score, hotel_name))



