"""
Question:
Maintain product stock and notify when inventory falls below a minimum threshold.
"""

stock = int(input("Enter Current Stock: "))
minimum = int(input("Enter Minimum Stock: "))

if stock < minimum:
    print("Low Stock Alert")
else:
    print("Stock Available")
