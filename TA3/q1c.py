#
# Lucky Password Identifying Program (q1c.py)
#
# Purpose: This program consists of a function isLuckySeven(pwd) that can show whether a password(str format) (parameter pwd)
# is lucky or not based on Master Seven's fortune suggestion and security consideration. The conditions are as follows:
# 
# - Between 8 and 32 characters
# - Contains only uppercase, lowercase, digits, and the punctuations '+', '-', '*', '/'.
# - Contains at least one digit and only one of the punctuation characters.
# - Contains the substring '77' in the password at least once.
# 
# The program returns True if it is a lucky password and False otherwise.
# This question assumes that the parameter pwd is a string.
#
# Limitations: There is no validation on the input of the parameter - pwd. It is assumed to be of String type.
# There is no proper message or guideline shown to the user when the user-specific password does not satisfy
# the requirements based on Master Seven's fortune telling and security issues. Setting up an appropriate password
# would be difficult without proper message/suggestion.
# The program needs to be re-coded when the conditions change.
#
# Written by CHAN CHI HUNG (s12650050)
# On 13/03/2022
# For COMP S258 Assignment 3
#

def isLuckySeven(pwd):
    # Define sub_string as '77', allow future change instead of hard-coding
    sub_string = '77'
    
    # Punctation set for checking
    punct_set = ['+', '-', '*', '/']
    
    # counters for digits and punctuation characters
    digit_count = 0
    punct_count = 0
    
    # Check condition 1 - password length between 8 and 32 characters
    # When False, no need to compare substring or each character one by one, save CPU resources and time.
    # return False directly
    if len(pwd) < 8 or len(pwd) > 32:
        return False
    
    # Check condition 4 - if substring 77 appears at least once or not.
    # When False, no need to compare each character one by one, save CPU time, return False directly.
    elif sub_string not in pwd:
        return False
    
    # Satisfy conditions 1 and 4, further check the conditions 2 and 3
    # It involves searching and count for each character, check when conditions 1 and 4 are okay to save CPU resources
    # Loop each character in the password string pwd and check.
    else:
        # Loop each character in the password
        for i in pwd:
            # Counter + 1 when the character is a digit
            if i.isdigit():
                digit_count += 1
            
            # Counter + 1 when the character is a digit
            elif i in punct_set:
                punct_count += 1
            
            # If the character is not digit and punctations, but alphabet in lowecase, uppercase
            # Pass and check the next character
            elif i.islower() or i.isupper():
                continue
            
            # The character is not a digit, punctuation, alphabet with uppercase or lowercase
            # Violate condition 2, no need to continue, return False directly
            else:
                return False
        
        # Pass the for-loop without return False, satisfy condition 2 and now check condition 3
        # If at least one digit and only one punctuation, all conditions are met, return True
        if digit_count >= 1 and punct_count == 1:
            return True
        
        # Condition 3 not met, return False
        else:
            return False
                
# TEST CODE
testcases1 = ['ABCDEF', 'ABCDEFGH', 'ABCDabcd', 'ABCD ']
testcases2 = ['ABCDef77@', 'ABCDef777+']

for t in testcases1:
    t = str(t)
    print(isLuckySeven(t))

for t in testcases2:
    t = str(t)
    print(isLuckySeven(t))
    