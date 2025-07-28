# Day 5 of Python Coding Challenge
# Today's exercise focused on building a simple discount calculator. 
# The function my_discount():
# Prompts the user to input the original price and the discount percentage.
# Calculates the final price after applying the discount.
# Returns the discounted price.
# This task helped reinforce concepts like user input, arithmetic operations, and formatted output. 
# Check out the output for a price of 150 and a discount of 15% in the terminal! 

def my_discount(amt,dis):
    
    percentage_dis = dis/100
    percentage = amt*percentage_dis
    actual_price = amt-percentage
    
    return actual_price

amount = int(input("Enter the amount : "))
discount = int(input(f'Enter the discount percentage : '))

print(my_discount(amount,discount))