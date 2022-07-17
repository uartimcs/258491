#
# Compounding calculation program (q2b.py)
#
# Purpose: This program is to use a while loop structure to print the savings after each number of months
#
# Limitation: No error checking.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 05/11/2021
# For COMP S258 Assignment 1 q2b
#

# User input the target saving.
# String type, change to float type using float()
target_saving = float(input("Enter target ($): "))

# Principal is set as $10,000
PRINCIPAL = 10000

# Variable for store the total saving
total_saving = 0

# Set a counter for while loop, initialize with 0
counter = 0

# At 0 month, total saving is equal to principal
total_saving += PRINCIPAL

# Count the total saving using while loop.
while (total_saving < target_saving):
    total_saving *= 1.15
    counter += 1
    print("After {} months saving is ${}".format(counter,total_saving))

# Print the months required to reach input value    
print("Reached ${} after {} months".format(target_saving,counter))