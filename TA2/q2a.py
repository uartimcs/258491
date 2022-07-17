#
# Company Name Fortune-telling Program(q2a.py)
#
# Purpose: This program can determine whether a company name is considered a good or bad fortune company name based on
# the advice of the famous fortune-teller, Dr.Seven. 
#
# This program has a function isGoodFortune(name) with an input str parameter name representing the name of a company
# in capital letter.
#
# The function will decide whether the company name is fortune or bad based on famous fortune teller Dr. Seven's definitions, including
# occurence of evil letter(s) and counting the number of 'good letters' and 'bad letters'.
# The function returns True if it is a good name, returns False when it is a bad name and returns None when the input name is not a string.
# 
# Limitations: The program required has no input console for the user to enter the company name
# The company name must be hard-coded in the program.
# This program assumes that company name contains only uppercase letters and spaces. In reality it is not the case.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 04/02/2022
# For COMP S258 Assignment 2
#

def isGoodFortune(name):
    
    # Evil Letters Set
    evil_letters = ['E','V','I','L']
    
    # Bad Letters Set
    bad_letters = ['B','A','D'] + evil_letters 
    
    # Counters for good letters and bad letters
    good_count = 0
    bad_count = 0
    
    # Fortune result, assume False, bad name
    status = False
    
    # Program Documentation
    # An empty string has the type of str as well. 
    # 'Has more good letters than bad letters' -> should return False if empty str used as company name (looks ridiculous)
    # I don't use try..except because there is no intention/necessity of change in data type.
    
    # if it is not a str, return None.    
    if(type(name) != str):
        return None
    
    else: 
        # Loop each character in the company name
        for x in name:
            
            # if any char is in the list of evil, no need to continue and return False. 
            if x in evil_letters:
                
                status = False
                return status
            
            elif x in bad_letters:
                
                # if and elif are mutually exclusive. This part only works with string containing 'B' , 'A' and 'D'                 
                # + 1 for bad count if met a bad letter
                bad_count += 1
            
            elif x == ' ':
                # Empty space, continue, not count towards bad or good letters
                continue
            
            else:
                # + 1 for good count if met a good letter
                # since we assume the name contains space and uppercase letters only
                # if it is not evil, not bad, not space, then it must be in good letters
                good_count += 1
                
                
        # after for loop of each letter in name, compare good letters and bad letters number counts
        if good_count > bad_count:
            status = True
            
        else:
            status = False
        
        return status

# demonstrate examples of the functions
print(isGoodFortune("GGE"))
print(isGoodFortune("GGV"))
print(isGoodFortune("GGGI"))
print(isGoodFortune("LGGGG"))
print()
print(isGoodFortune("GGGGGGG"))
print(isGoodFortune("BADGGGG"))
print(isGoodFortune("AAGGG"))
print(isGoodFortune("GGAAAGG"))
print(isGoodFortune("BADGGG"))
print(isGoodFortune("GAAAG"))
print(isGoodFortune(""))
print()
print(isGoodFortune(None))
print(isGoodFortune(123))

