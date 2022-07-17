#
# Mangos total price calculation program (enhanced version) (q1f.py)
#
# Purpose: This program is to calculate the amount to pay for the mangos purchased. 1 Free for >=10 Mangos
#
# Limitation: There is no error checking for the user's input. 
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q1f
#

# Give an input instruction to the user and allow the user to input the mangos purchased in the console.
# data type is string , convert it to int type using int()
mango_number = int(input("Enter the number of super mangos: "))

# mango price is treated as constant, $10.50
MANGO_PRICE = 10.50

# When user purchases 10 or more mangos, 1 for free.
# Number of mango needs to pay reduces by 1.
if mango_number >= 10:
   mango_number -= 1

# total price = mango price * price per mango
total_price = MANGO_PRICE * mango_number

# Output the total price with dollar sign, 2 decimal places
print("Amount to pay is ${:.2f}".format(total_price))
