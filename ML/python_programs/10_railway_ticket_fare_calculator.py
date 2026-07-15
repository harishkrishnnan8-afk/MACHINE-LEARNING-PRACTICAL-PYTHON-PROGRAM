"""
Question:
Calculate ticket fare based on age, class, and available concessions.
"""

fare = float(input("Base Fare: "))
age = int(input("Age: "))
cls = input("Class (Sleeper/AC): ")

if cls.lower() == "ac":
    fare += 500
else:
    fare += 200

if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7

print("Total Ticket Fare =", fare)
