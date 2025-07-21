# Day 2: Strings to Integers

# Today’s challenge was all about working with data conversions in Python. 
# Task: Write a function called `convert_add` that: 
# - Takes a list of strings as input. 
# - Converts the strings into integers. 
# - Returns the sum of the list. 

# For example, the input `['1', '3', '5']` becomes `[1, 3, 5]`, and the function outputs `9`.

def convert_add(lst):
    convrt = [int(i) for i in lst]
    return sum(convrt)

print(convert_add(['1','3','5']))

