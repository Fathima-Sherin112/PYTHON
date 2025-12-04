# Day 8 of Python Coding Challenge:
# Today's task was to write a function only_floats(a, b) that checks the number of float inputs provided:
# Returns 2 if both inputs are floats.
# Returns 1 if one input is a float.
# Returns 0 if neither input is a float.
# This was a fun exercise in using Python's isinstance() function to perform type checking! 📚

def only_floats(a,b):
    if isinstance(a,float) and isinstance(b,float):
        print("both are float")
    elif isinstance(a,float) or isinstance(b,float):
        print("one is float")
    else:
        print("none are float")
    
num1 = 1.55
num2 = 2.44
print(only_floats(num1,num2))