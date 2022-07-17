#
# Bird seed block price calculation program (q1e.py)
#
# Purpose: This program is to calculate the price of a bird seed block with user-defined dimensions.
#
# Limitation: There is no error checking for the user's input. 
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q1e
#

# Open message
print("Made-to-measure seed block")

# Allow users to input length, width and height
# String type, convert to float pt type using float()
length = float(input("Enter the length(m): "))
width = float(input("Enter the width(m): "))
height = float(input("Enter the height(m): "))

# Calculate volume of block in cubic meter
volume = length * width * height

# The price per cubic meter is $550,000, constant term
PRICE_PER_VOLUME = 550000

# Calculate the price, based on $550,000 per cubic meter
price = volume * PRICE_PER_VOLUME

# Output the total price with dollar sign, 2 decimal places
print("The price is ${:.2f}".format(price))