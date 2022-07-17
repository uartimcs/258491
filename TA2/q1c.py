#
# Restaurant 'Bias Burger' price printing program (q1c.py)
#
# Purpose: This program can show the price of a 'Bias Burger' in the restaurant based on the student's GPA in the university.
# Students with different ranges in GPA will get their burger in the restaurant at different prices.
# Error checking and input validation of GPA value are built-in to prevent certain common invalid input,
# i.e. empty input, not a number, invalid GPA values from user.
# The program will ask the student to re-enter GPA until the input is valid.
#
# Limitations: The program shows the price of one 'Bias Burger'. If the students want to buy more,
# he/she needs to calculate the total price by his/her own. There is no input of number of 'Bias Burger' provided.
# There is no exit point in the program. The program requires the user to re-enter until the value is valid.
#
#
# Written by CHAN CHI HUNG (s12650050)
# On 03/02/2022
# For COMP S258 Assignment 2
#

# Keep track of status of while-loop.
status = True

while status:
    
    # allow the user to input the GPA.
    input_gpa = input('Enter GPA: ')
    
    try:
        # Check Empty input
        if not input_gpa:
            print('The input is empty')
            
        else:
            # Convert the GPA data type from str to float
            # if the input is not a number. The conversion is failed and ValueError exception would be caught.
            gpa = float(input_gpa)
            
            # Check GPA values to ensure it is valid.
            if gpa < 0:
                print('The GPA should be positive')
                
            elif gpa < 2.0 or gpa > 4.0:
                print('The GPA should be >= 2.0 and <= 4.0')
                
            else:
                # Pass the validation tests, GPA data available to be used
                # Exit the while-loop after passing GPA validation.
                status = False
                
    except ValueError:
        # Error message printed for not a number 
        print('The input is not a number')

# variable for 'Bias Buger' price, default as 0.
burger_price = 0

# GPA conditions check
if gpa >= 3.5:
    burger_price = 50
    
elif gpa >= 3.0 and gpa <3.5:
    burger_price = 45
    
elif gpa >=2.5 and gpa < 3.0:
    burger_price = 40
    
else:
    # after validation, the else part represents GPA >= 2.0 and GPA <2.5   
    burger_price = 35

# print the 'Bias Burger' price    
print('The price is ${}'.format(burger_price))        
        