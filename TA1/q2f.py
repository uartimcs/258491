#
# Indoor Air Pollution Index (IAPI) printing program (q2f.py)
#
# Purpose: This program is use to generate Indoor Air Pollution Index (IAPI) statistics
#
# Limitation: No error checking on strings/other invalid inputs.
# 
#
# Written by CHAN CHI HUNG (s12650050)
# On 06/11/2021
# For COMP S258 Assignment 1 


# Summation of input, for average count.
total_sum = 0.0

# holders for max, min and previous value.
max_value = 0
min_value = 0
previous_value = 0

# counters to count occurence/steps.
loop_count = 1
unhealthy_count = 0
healthy_count = 0
worse_count = 0

# open message
print("IAPI Analyser")

# Check day collect is not zero. Otherwise error when showing average value
nonzero_status = False

while nonzero_status == False:
    day_collect =int(input("Enter number of days of the IAPI data collection period: "))
    if day_collect != 0:
        nonzero_status = True


while loop_count <= day_collect:
    temp = float(input("Enter the daily IAPI of day {} : ".format(loop_count)))
    
    # if the input is not in the range, repeat the input
    while temp < 0.0 or temp > 20.0:
        print("Input Error: IAPI should be between 0 and 20.0")
        temp = float(input("Enter the daily IAPI of day {} : ".format(loop_count)))

    #valid input temp, add the value to total_sum to count average
    total_sum += temp

    # Counter + 1 for unhealthy condition
    if temp > 10.0:
            unhealthy_count += 1
            
    # Counter + 1 for healthy condition            
    if temp <= 2.0:
            healthy_count += 1     
            
    # max, min and previous value handling       
            
    # first value, assign this value to max, min and previous value for data comparison.
    if loop_count == 1:
        max_value = temp
        min_value = temp
        previous_value = temp
                 
    # else for comparing on-going inputs.
    else:
                    
        # Counter + 1 for worse condition         
        if temp > previous_value:
            worse_count += 1
        
        # swap max value if input is greater      
        if temp > max_value:
            max_value = temp
            
        # swap max value if input is smaller             
        if temp < min_value:
            min_value = temp
        # replace previous value with current temp value after comparison   
        previous_value = temp
        
    # complete the steps, loop counter + 1    
    loop_count += 1
    
    
# print out a list of required summary data
average = total_sum / day_collect
print("Average daily IAPI in the period:",average)
# print out the rest outcomes with variable and counters
print("Maximum daily IAPI is", max_value)
print("Minimum daily IAPI is", min_value)
print("Number of days with Very Unhealthy IAPI is", unhealthy_count)
print("Number of days with Healthy IAPI is", healthy_count)
print("Number of days with IAPI higher than previous day is", worse_count)