#
# Bitcoin Investment advice Program (q1e.py)
#
# Purpose: A program that allows Anders to enter 5-day period of Bitcoin rate sampled at 12 pm every day, analyze the highest rate, lowest rate 
# and average rate and provide Bitcoin investment advice to the user based on the set conditions, i.e.
# whether the day 5 rate is more than 20% above the average, more than 20% below the average or else.
# The program will check if input values are positive or not. If found non-positive,
# a suitable message is printed out and ask the user to re-enter.
#
# Limitations: This program only allows the user to input Bitcoin rate on 5 days. No input choice for the user to select
# e.g. 10-days, monthly or by year.
#
# Since BitCoin is a high-risky investment in crypto-currency. The rate fluctates a lot on the same day.  
# If the user applies margin or buy derivatives on these investments, great loss may result in if no percentage tolerance is set on the same day.  
# Certain warnings should be provided if the program is used as investment advice.
#
# Written by CHAN CHI HUNG (s12650050)
# On 03/02/2022
# For COMP S258 Assignment 2
#

# Default input days = 5
# Treat it as a constant term instead of hard-coded value
# We can amend the number of days when necessary.
INPUT_DAY = 5

# Create a list of size = INPUT_DAY, default values are all 0
# index from 0 to INPUT_DAY-1
rate_list = [0] * INPUT_DAY

# Prepare highest, lowest and average variables
highest = lowest = None
average = 0

for i in range(len(rate_list)):
    
    # Keep track of while-loop status.
    status = True
    
    while status:
        
        # allow the user to input the Bitcoin rate at i+1 day
        input_value = input('Enter Bitcoin rate of day {}'.format(i+1) + "(USD): ")
    
        try:
            # Check Empty input
            if not input_value:
                print('The input is empty')
                
            else:
                # Conversion of data type. if input is not a number, exception ValueError caught and re-enter.
                input_value = float(input_value)
                
                if input_value > 0:
                    
                    # Positive number. Valid. Assign the input value to the correpsonding element in the list.
                    rate_list[i] = input_value
                    
                    # ready for enter next day, exit while-loop and for next day input.
                    status = False
                    
                # if input value is negative, print message and re-enter     
                else:
                    print('The Bitcoin rate should be positive')
                    
        except ValueError:
            
            # catch the exception of ValueError and print message to notify the user
            print('The input is not a number. Please try again.')
                            
            
# Use the built-in functions for num list to get highest, lowest and average values in the list
highest = max(rate_list)
lowest = min(rate_list)

# Get the average value of the num list using sum() and len()
# average is certain to be present after input validation.
average = sum(rate_list)/ len(rate_list)

# print the analysis result
print('The highest rate is {}'.format(highest))
print('The lowest rate is {}'.format(lowest))
print('The average rate is {}'.format(average))

# Extract day 5 Bitcoin value from the list
day_five = rate_list[4]

# Print the investment based on conditions provided.
if day_five < average * 0.8:
    print('BUY')
    
elif day_five > average * 1.2:
    print('SOLD')
    
else:
    print('HOLD')    





    