# Day 9: Coding Challenge
# Finding the Biggest Odd Number in Python
# Today, I worked on a Python function to find the biggest odd number in a string of digits. Here's how I solved it:
# 1️⃣ Used list comprehension to filter odd numbers from the input string.
# 2️⃣ Used the max() function to identify the largest odd number.
# 3️⃣ The result was printed in a clean and concise format.

# For example:
# 🔢 Input: '23569'
# 📊 Output: 9
# This challenge helped me improve my skills in list comprehension and string manipulation in Python.


def filter_max_odd (number):
    odd = [int(i) for i in number if int(i)%2!=0]
    return max(odd) 
print(filter_max_odd('23569'))