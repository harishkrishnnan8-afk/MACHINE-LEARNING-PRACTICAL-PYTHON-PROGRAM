"""
Question:
Check whether a password satisfies length, uppercase, lowercase, digit, and special character requirements.
"""

password = input("Enter Password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
