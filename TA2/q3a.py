#
# MetroMini minibus operation simulation program (q3a.py)
#
# Purpose: This program is to determine how many minibuses should be allocated each day for profit maximization in MetroMini minibus
# route between the university in Homantin and Hung Hom railway station using simulation based on 
# past passenger statistics and a profit/loss calculation function
#
# This program consists of three functions. The first function involves the use of past minibus passenger ststistics/probabilty
# to generate number of passengers based on the probability distribution.
# 
# The second function involves the cost-benefit analysis. We create a function that can calculate the profit/loss based on
# input number of minibus and number of passengers generated in the 1st part.
#
# The third function is to simulate the routine mini-bus transportation given that the input of minibus ranges from 1 to 30
# Through running each minibus input by 100000 times with random passengers set, we can get the optimization result that leads to profit maximization.
#
# Limitations: This program has a generalized probability distribution. In reality, the data may be fluctated through months and seasons
# or existence of new competitors (e.g. MTR, KMB)
# The program use Python random module to generate random numbers for simulation of passengers. 
# In fact, those random numbers are pseudo-random only.
# This program is set based on ideal case. For example, each minibus can run maximum of 16 times every day.
# There are peek hours and off-peak hours for transportation. minibuses may not be fully utilized.
# The distribution is discrete, i.e. increment of 500. There is no 1400 passengers but in reality there is.
#
# Written by CHAN CHI HUNG (s12650050)
# On 04/02/2022
# For COMP S258 Assignment 2
#

# import the random module for random numbers 
import random
# import the time module for seeding the random numbers 
import time
# import the math module for math calculation
import math

# randPassenger()
# randomly returns passengers according to probabilities
def randPassenger():
    
    # List of passengers and list of probability distribution for each set of passengers
    pass_gen = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
    prob = [0.01, 0.02, 0.08, 0.13, 0.18, 0.21, 0.21, 0.10, 0.04, 0.02]
    
    # random generate a float number from 0 to 1 inclusive.
    num = random.uniform(0,1)
    
    # create a list of cumulative probabilities
    cum_prob = [0] * 10
    
    # Generate the cumulative probabilities, i.e. P(Value <= pass_gen[i])
    for i in range(0, len(prob)):
        sum = 0
        for j in range(0, i+1):
            sum += prob[j]            
        cum_prob[i] = sum
    
    #print(cum_prob)
    # [0.01, 0.03, 0.11, 0.24, 0.42, 0.63, 0.84, 0.94, 0.98, 1.00]
    # sum of all probabilities of outcomes = 1
    # select pass_gen[i] as the return when the random number is
    # greater than pass_gen[i-1] and smaller than pass_gen[i]
    # The size ressembles the distribution required.
    
    # the number of passengers selected, default as 0.
    selected = 0
    
    # pass_gen[0] is a special case including >= 0 to be considered
    if num >= 0 and num < cum_prob[0]:
        selected = pass_gen[0]
    else:
        for i in range (1, len(cum_prob)):
            
            # e.g. if num > 0.01 and num <= 0.03, return pass_gen[1] - 1500
            # e.g. if num > 0.03 and num <= 0.11, return pass_gen[2] - 2000
            if num >= cum_prob[i-1] and num <= cum_prob[i]:
                selected = pass_gen[i]
                break
            
    return selected

#print(randPassenger())
# debug use (run 100000 times, calculate the average passenger generated)              
#sum = 0
#for j in range (0, 100000):
    #result = randPassenger()
    #sum += result
#print(sum/100000)
# The result closes to the expected value of the distribution, i.e. around 3400.
    
            
# simulateOneDay(numOfMinibus)
# Calculate and return the profit (or loss) made by the company 
# by simulating the number of passengers available in one day
def simulateOneDay(numOfMinibus):
    
    # Data set provided in the question
    # Hold in the form of constant instead of hard-coding for future re-programming
    # The constant variables are named self-descriptive
    BUS_CAPACITY = 19
    FUEL_COST = 27
    WAGE = 620
    DEPRE_COST = 264
    MAINTENANCE = 35
    WORK_HOUR = 8
    TRAVEL_TIME = 0.5
    BUS_FARE = 7.5
    
    # Set up basic equations/relations
    bus_run = int(WORK_HOUR/TRAVEL_TIME)
    max_capacity = bus_run * numOfMinibus * BUS_CAPACITY
    
    # generate the number of passengers using the randPassenger() function    
    pass_num = randPassenger()
    
    # dependent variables (depends on number of passengers and number of minibus allocated)
    # actual passengers served and actual number of run of minibuses, initialize as zero.
    actual_pass = 0
    actual_run = 0
    
    # Case 1: Passengers > max capacity
    # no sufficient minibus to serve passengers
    if pass_num > max_capacity:
        
        # bus run at full capacity
        actual_pass = max_capacity
        actual_run = numOfMinibus * bus_run
    # Case 2: Passengers <= Max capacity
    else:
        # all passengers can use minibuses
        actual_pass = pass_num
        # actual run => number of passengers / bus capacity, rounds up to the nearest integer
        actual_run = math.ceil(pass_num / BUS_CAPACITY)
        
    # Set up profit equation
    revenue = BUS_FARE * actual_pass
    cost = (WAGE + DEPRE_COST + MAINTENANCE) * numOfMinibus + FUEL_COST * actual_run
    profit = revenue - cost
    
    return profit


# findMaxProfit() 
# finds out how many minibuses should be allocated so that the profit is maximized
# by arranging different number of minibuses (1-30) and run simulation 100000 times.
def findMaxProfit():
    
    # set the number of stimulation
    SIMULATION_TIME = 100000
    
    # record Max profit
    max_profit = 0
    # record of corresponding minibuses lead to max profit
    minibus_max = 0
    # record the average profit leading to profit maximization
    average_profit = 0
    
    # minibuses (1 - 30)
    for i in range(1, 31):
        
        # set a counter to sum all profit outcomes in 100000 times
        count = 0
        for j in range(0, SIMULATION_TIME):
                       
            # generate profit/loss for i minibus in service
            result = simulateOneDay(i)
            # add the result to total profit counter
            count += result
            
        # After the loop, evaluate the average profit for minibus i
        average_profit = (count/SIMULATION_TIME)        
        # print the average profit for each possible number of minibus
        print('The average profit for {} minibus(es) is ${:.2f}'.format(i, average_profit))
        
        if average_profit > max_profit:
            max_profit = average_profit
            minibus_max = i
        
    # print the number of minibuses that can maximize the average profit.
    print('the number of minibuses that can maximize the average profit is {}'.format(minibus_max))
    
# Set a fixed random seed
# random.seed(0)
# This is to ensure that each for-loop uses the same 100000 sets of numbers for different minibuses
# Direct comparison. Cannot compare A and B fairly if they do not share the same set of numbers.
# Use 0 will cause each execution the same results. we can assign other value each time to make the execution slightly different
# e.g.
rt = time.time()
random.seed(rt)

# Call function to find results
findMaxProfit()







