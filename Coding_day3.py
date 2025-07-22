# Day 3 of Python Coding Challenge: 
# Wrote a simple function to count the number of students present based on a register. 
# Key takeaway: Iterating over dictionary values is super useful! 

# Write a function called register_check that checks how many students are in school. 
# The function takes a dictionary as a parameter. If the student is in school, the dictionary says 'yes'. 
# If the student is not in school, the dictionary says 'no'. Function should return the number of students in school.

# Example:-
# register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
# From Above dictionary . function should return 3.

def register_check(dic):
    count = 0
    for i in dic.keys():
        if dic[i]=='yes':
            count+=1
    return count
reg = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(reg))