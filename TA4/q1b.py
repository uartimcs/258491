#
# Palindrome Recognition Program (q1b.py)
#
# Purpose: A palindrome is a string that reads the same when reversed. 
# Spaces are ignored, and the case of the letter is irrelevant to determine if a string is a palindrome. 
# This program can receive an input from the user and determine whether the input is a palindrome
# or not using the function isPalindrome and the data structure - stack module from pyListStack
# 
# Limitations: The function classifies whether a string is a palindrome by set conditions. 
# If there is any change,the function has to be re-programmed. 
# This program involves importing a data structure - Stack from self-defined class pyListStack 
#
# Written by CHAN CHI HUNG (s12650050)
# On 01/05/2022
# For COMPS258 Assignment 4
#

# import the Stack module from self-defined pyListStack
# it is user-defined, must be in the same directory before execution
from pyListStack import Stack

# isPalindrome(aString) function
def isPalindrome(aString):
    
    # Create an empty stack
    s = Stack()

    # Store the previous added character, initialized as None first
    # use the peek(), but need to handle the case when the stack is empty.
    previous_ch = None
    
    # The string with characters added to the stack sequentially.
    # reversedText generated from popping the stack will compare with truncatedText
    # If they are equal, then the string is a palindrome.
    truncatedText = ""
    
    # Convert all Uppercase letters to Lowercase first
    # checkString = aString.replace(" ","").lower()
    # CC replied on the discussion board that consecutive letters should be handled first than spacing
    checkString = aString.lower()
    
    # Check every character in the String
    for ch in checkString:
        # Check if character ch is an alphabet
        if ch.isalpha():
            # if letter is added previously, ignore and compare the next character
            if previous_ch == ch:
                continue
            
            # push it on top of stack
            # Add the character to the truncatedText and record it
            else:
                s.push(ch)
                truncatedText += ch
                previous_ch = ch
  
            #ignore all the digits, punctuations and other non-letter characters
            
    #print(truncatedText)    
                
    reversedText = ''
    # Continue to pop the character from the stack in FIFO way
    while not s.isEmpty():
        reversedText = reversedText + s.pop()
    
    # When all characters in the string is not letter, an empty string is result in.
    # It should not be considered as a Palindrome.
    if len(truncatedText) == 0:
        return False
    
    # Compare the truncatedText and reversedText, True when equal
    return truncatedText == reversedText


if __name__ == '__main__':
    negative_examples = ['AB', 'aAABb']
    positive_examples = ['A', 'AAa', 'AAAABBA', 'AaaBBaaaA', 'A78124832838989898934938928439A', 'A23904239483298*$#(*($#**$(#    A']

    while True:
        userText = input("Please enter the text you want to check (<ENTER> to quit): ")
        if len(userText) == 0:
            break
        if isPalindrome(userText):
            print("yes")
        else:
            print("no")
    print("Till next time!")