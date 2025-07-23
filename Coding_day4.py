# Day 29: Middle Figure in Python!
# Today's challenge was about writing a function that takes two strings, joins them, and finds the middle element. 
# If the combined string has a middle element, the function returns it; otherwise, it returns "no middle figures".
# 🔹 Features Implemented:
# ✅ Removes spaces before joining the strings
# ✅ Checks if the combined string length is odd or even
# ✅ Returns the middle character if length is odd
# ✅ Returns "no middle figures" if length is even
# 🔥 Challenge Breakdown:
# 🔸 Remove spaces from both strings
# 🔸 Concatenate them into a single string
# 🔸 Find the middle character using indexing
# 🔸 Return the middle element if odd, else return "no middle figures"
# Example Runs:
# Input: make love, not wars
# Output: e
# Input: good, luck
# Output: no middle figures

def middle_figure(a,b):
    a = a.replace(" ","")
    b = b.replace(" ","")
    sentance = a+b
    #print(sentance)
    total_len = len(sentance)
    #print(total_len)
    if total_len%2==0:
        return "no middle figure"
    else:
        return sentance[total_len//2]
    

text1 = input("enter string1 : ")
text2 = input("enter string2 : ")
print(middle_figure(text1,text2))



