"""
Question:
Determine donor eligibility based on age, weight, and hemoglobin level.
"""

age = int(input("Enter Age: "))
weight = float(input("Enter Weight: "))
hb = float(input("Enter Hemoglobin: "))

if age >= 18 and weight >= 50 and hb >= 12.5:
    print("Eligible to Donate Blood")
else:
    print("Not Eligible")
