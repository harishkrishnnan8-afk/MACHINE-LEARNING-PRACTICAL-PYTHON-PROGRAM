"""
Question:
Calculate fuel expense for a trip based on distance, mileage, and fuel price.
"""

distance = float(input("Enter Distance (km): "))
mileage = float(input("Enter Mileage (km/l): "))
price = float(input("Enter Fuel Price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel Required =", fuel)
print("Fuel Cost =", cost)
