"""
Question:
Determine whether a citizen is eligible to vote based on age and nationality.
"""

age = int(input("Enter Age: "))
nation = input("Enter Nationality: ")

if age >= 18 and nation.lower() == "indian":
    print("Eligible to Vote")
else:
    print("Not Eligible")
