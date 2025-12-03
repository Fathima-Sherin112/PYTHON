# Day 8: Coding Challenge 
# Analyzing Odd and Even Numbers in Python
# Today, I worked on a Python function to compute the difference between the maximum even number and the minimum odd number in a list.
# Here's a breakdown of the task:
# 1. Segregated the numbers into even and odd categories using a loop.
# 2. Calculated the maximum even and minimum odd values.
# 3. Derived the difference between these two values and printed the result.
# This exercise helped me refine my understanding of list operations and conditional logic in Python.


# Input: [1, 2, 4, 6]
# Output: "The difference is 5"
 
# input = [1,2,4,6]
# even = []
# odd = []
# for i in input:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# diff = max(even)-min(odd)
# print(diff)

def even_odd(input):
    even = [i for i in input if i%2 == 0]
    odd = [i for i in input if i%2 != 0]
    diff = max(even)-min(odd)
    return diff
input=[1,2,4,6]
print(even_odd(input))