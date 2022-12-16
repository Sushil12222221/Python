# WAP to check whether a password is valid or invalid

import re
str = input("Enter password to check: ")
if(re.match(r"(?=.*[A-Z])(?=.*[@$])(?=.*[0-9])[a-zA-Z0-9@$]{8,}",str)):
    print("Valid password")
else:
    print("Invalid password")
