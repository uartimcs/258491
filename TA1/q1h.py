#
# MU Name Cards price calculation program (q1h.py)
#
# Purpose: This program is to calcute the amount to pay for a customer ordering name cards.
#
# Limitation: No details of error input for validation
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q1h
#

# open message
print("MU Name Cards")

# Allow users to input paper type, colour and lot numbers.
# String type, convert to int type for variables colour and lots.
paper_type = input("Enter the required paper type (A, B, C): ")
colour = int(input("Enter number of colours : "))
lots_number = int(input("Enter number of lots of 500 : "))

# Initialization of price variable
price = 0.0

# Error indicator for the inputs
error_prone = False

# Check lots number, if it is > 0.
# Show error prone when <= 0
if lots_number <= 0:
   error_prone = True

# Check type and colour 
# if matches, show corresponding price in table matrix. If not, gives error prone
if paper_type == 'A':
    if colour == 1:
        price = 140.0
    elif colour == 2:
        price = 180.0
    elif colour == 4:
        price = 250.0
    else:
        error_prone = True
        
elif paper_type == 'B':
    if colour == 1:
        price = 100.0
    elif colour == 2:
        price = 120.0
    elif colour == 4:
        price = 160.0
    else:
        error_prone = True
        
elif paper_type == 'C':
    if colour == 1:
        price = 80.0
    elif colour == 2:
        price = 90.0
    elif colour == 4:
        price = 120.0
    else:
        error_prone = True    
        
else:
    error_prone = True

# if error prone is true, show error msg instead of print out amount to pay
if error_prone == True:
    print("Error in the input")
else:
# calculate total price and output, no decimal places shown.
    total_price = price * lots_number
    print("The amount to pay is ${:.0f}".format(total_price))


