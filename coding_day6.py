# Today’s task: Extracting usernames from email addresses!
# 🔹 Validates user input for an @ symbol.
# 🔹 Extracts the username (everything before @).
# 🔹 Keeps prompting until a valid email is entered.

# Simple, effective, and a great intro to input validation & string manipulation in Python! 
 
def email():
    mail = input("Enter the email : ")
    while "@" not in mail:
        print("Invaild mail address")
        mail = input("Enter the email : ")
    return mail.split("@")[0]

print(email())




