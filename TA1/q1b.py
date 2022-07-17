#
# Birthday celebration message program to the user (q1b.py)
#
# Purpose: This program is to print Happy birthday messages using user's input name.
#
# Limitation: Invalid input may go in. There is no error checking for the user's input. 
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q1b
#

# Show an input instruction to the user's console
# Allow the user to input the name 
input_name = input("Enter your name: ")

# Print the celebration message containing user's input name.
print("Happy birthday to me. Happy birthday to me.", "Happy birthday to {}.".format(input_name), "Happy birthday to me!")



