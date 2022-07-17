#
# Money Breaking Down Program (q1b.py)
#
# Purpose: This program can break down a given amount of money into the standard denominations of $1 or more.
# The standard denominations include $1000, $500, $100, $50, $20, $10, $5, $2, $1. 
# No one likes $1000 banknote because it is difficult for change in transactions. Hence we omit $1000 here.
#
# The program first allows the user to input the amount of money to be broken down.
# If the input is valid, it breaks down the amount into banking notes anc coins accordingly to make sure
# the changes have minimal number of bank notes and coins.
# After output, it allows the user to continue or exit from the program by typing 'y' or 'n'.
#
# Limitation: The set of standard denominations is pre-defined in program codes and specialized for Hong Kong.
# It is not applicable for other currencies, e.g. RMB banknote has the greatest face value of 100 only.
# Korean WON banknote, on the other hand, has the greatest face value of 50,000.
# Second, this program does not support breaking down of money with values below $5.
# 
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

# Keep the running status of main program
status = True
while status:
    try:
        # Allow the user to input the amount to break down
        # Try to convert the input to int or catch ValueError (e.g. no input, float no, mix of number and str..etc)
        amount = int(input('Enter the amount you wish to break down: '))
        
        # Ok for type conversion - int
        # then check if amount is less than $5. We don't accept change lower than $5.
        if amount < 5:
            print('Amount cannot be less than $5. ')
        
        else:
            # Create a list of available denominations for change use.
            # Although dictionary is more convenient, I prefer use of list, as long as it works.
            # It is arranged from the greatest to smallest denomination
            dollar_list = [500, 100, 50, 20, 10, 5, 2, 1]
            
            # Create a list to hold the number of banknotes/coins in each denomination in the dollar_list
            # The list size is the same as the size of dollar_list
            
            # Set all notes changed are 0 by default before changing begins.
            change_list = [0] * len(dollar_list)
            
            
            for i in range(0, len(dollar_list)):
                
                # Get the number for each value of banking note, from $500 to $1
                # Use floor division in Python to get integer value, or quotient 
                change_temp = amount // dollar_list[i] 
                
                # Store the bank notes amount in the corresponding element/container in the change_list
                change_list[i] = change_temp
                
                # Remained amount/Remainder for further operations of change of banknotes until the loop is completed
                # Sicne the input amount is integer, finally it must be zero because the minimum unit is $1.
                # No extra operation is needed after for loop, amount must be zero at the end.
                amount = amount % dollar_list[i]
                #print(amount)
                
            # Output result
            print("Here's your change: ")
            
            for j in range (0, len(dollar_list)):
                
                # When the number is 0 for a particular face value of banking note, skip and not shown in console.
                if change_list[j] == 0:
                    continue
                
                # Print the banking notes face value and the number using format specified in question
                else:
                    print('$ {} : {}'.format(dollar_list[j], change_list[j]))  
                
                            
    except ValueError:
        # Print the alert when the input is not valid, e.g. no input, fractions, string 
        print('Please enter a valid dollar amount (whole numbers only).')
        
    # No matter the program runs or with Error, it reaches the retry status, i.e. continue or exit
    # This status keeps track of the retry part of the program
    retry_status = True
    while retry_status:
        # Allow the user to continue or exit the program
        confirm = input('Want to enter another amount (y/n): ')
        
        # if answer is yes, escape the retry while loop and continue
        if confirm == 'y':
            break
        
        # if answer is no, show goodbye message and end the program
        # Exit both the retry while-loop and main program while-loop
        elif confirm == 'n':
            print('Bye and see you next time.')
            retry_status = False
            status = False
       
        # Not y or n, re-ask until the user types y or n
        # optional, The handling is not specified in the question
        else:
            continue
            
        