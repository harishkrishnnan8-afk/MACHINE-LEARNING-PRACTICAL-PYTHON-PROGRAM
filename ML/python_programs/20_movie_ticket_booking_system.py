"""
Question:
Calculate ticket cost based on number of seats, seat category, and applicable discounts.
"""

seats = int(input("Enter Number of Seats: "))
category = input("Enter Category (Silver/Gold): ")

if category.lower() == "gold":
    price = 250
else:
    price = 150

total = seats * price

if seats >= 5:
    total *= 0.90

print("Total Ticket Cost =", total)
