#
# Chicken pieces total price calculation program (q1g.py)
#
# Purpose: This program is to calculate the final amount payable given the number of chicken pieces.
#
# Limitation: If you input wrongly, you have to relaunch the program.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021 v2
# For COMP S258 Assignment 1 q1g
#

# Open message
print("Metro Chicken")

# Price per chicken 
chicken_price = 15

# Give an input instruction to the user and allow the user to input the chicken pieces purchased.
# String type, convert to int type using int()
number_of_chicken = int(input("Enter the number of chicken pieces: "))

# Check the user's input. If input is invalid (<= 0), print msg and quit (will not do else part)
if number_of_chicken <= 0:
   print("Sorry the input is not an integer")
   
else:
    # Condition 1:  0 < chicken <= 6 , original price
    if number_of_chicken <= 6:
        total_price = number_of_chicken * chicken_price
        
    # Condition 2: chicken >= 7, $3 discount given from 7th chicken  
    elif number_of_chicken >= 7:
        total_price = 6 * chicken_price + (number_of_chicken - 6) * (chicken_price - 3)
    
    # discount when total spent >= 200. It can fuse to elif part because total price for 6 chickens is just $90. no discount on if part.
    # But it is possible that the price of chicken will get higher due to inflation later. So separately consider.
    if total_price >= 200:
        total_price = total_price * 0.9
    
    # print the final charge in 2 decimal places.
    print("Amount to pay is ${:.2f}".format(total_price))