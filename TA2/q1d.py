#
# Casino Dice Rolling Simulation Program (q1d.py)
#
# Purpose: This program can simulate the results of rolling three dices by 1000 times in the Ngak Yan Casino,
# provided that one die is purposely replaced by a cheat die with the '6' face replaced with a '5' face.
# The program uses the built-in random module in Python to generate random numbers to simulate the rolling result
# of three dice and generates the outcome statistics using numbers and a diagram with '*' to represent the population
# in each rolling outcome.
#
# Based on probability theory, as the number of rolling increases, the outcome will approach the theoretical
# probability distribution. If a disrupted distribution is found, it may indicate the presence of cheating
# in the Casino.
#
# Written by CHAN CHI HUNG (s12650050)
# On 03/02/2022
# For COMP S258 Assignment 2
#

# import the random module for random numbers and built-in functions
import random

# Programm Documentation
# The sum of rolling three normal dices ranges from 3 to 18. Thus, no of possible outcomes = (18-3) + 1 = 16
# with one cheated die used, the range is from 3 to 17.
# But the Casino must assert all dice are normal to the gamblers.
# To verify it, we should add 18 in the outcome range to show that the Casino uses cheated dice.
# Under such case, the appearance of 18 must be zero when a cheat die is used.


# Create a list of size of 16, default values are all 0
# This list is used to count number of each outcome ranging from 3 to 18
dice_sum = [0] * 16

# Simulate rolling three dices 1000 times.
for i in range (0, 1000):
    #simulation of rolling the first die (normal die), 1-6 (inclusive)
    dice_one = random.randint(1,6)
    
    #simulation of rolling the second die (normal die), 1-6 (inclusive)
    dice_two = random.randint(1,6)

    #simulation of rolling the third die (cheat die), repeating five.
    dice_three = random.choice([1,2,3,4,5,5])  
    
    # Get the sum points of dice
    result = dice_one + dice_two + dice_three
    
    # + 1 for a corresponding element in the list
    
    # dice_sum[0] represents occurence of sum = 3.
    # Hence dice_sum[n-3] presents occurence of sum = n, where n >= 3
    dice_sum[result-3] += 1

# print the header of the statistics outcomes
print('Sum','Freq') # occupy three spaces for 'Sum', four spaces for 'Freq'

# 16 elements, 0-15, representing sum = 3 to sum = 18
for j in range(0, len(dice_sum)):
    
    # The sum represented is equal to index + 3, e.g. dice_sum[0] => 0 + 3 = 3    
    s = j + 3
    
    # get the corresponding frequency/occurences
    freq = dice_sum[j]
    
    #To match the pattern, sum: field right aligned 2 spaces, frequency: right-aligned 5 spaces
    print('{:>2} {:>5} '.format(s, freq), end='')

    # Finally print the number of * using floor division, e.g. 58 => *****
    print('*'*(freq//10))