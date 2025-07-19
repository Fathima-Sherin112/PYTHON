# Today’s Task:
# Day 1: Division and Square Root
# Write a function called divide_or_square that takes a single number as input.
# If the number is divisible by 5, the function should return its square root. 
# If not, it should return the remainder when the number is divided by 5

import math
def divide_or_square(n):
    if n%5==0:
        return round(math.sqrt(n),2)
    else:
        return n%5
n=10
print(divide_or_square(n))