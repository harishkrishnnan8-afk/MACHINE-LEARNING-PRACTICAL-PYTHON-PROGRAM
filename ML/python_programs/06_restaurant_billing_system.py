"""
Question:
Generate customer bill including GST and service charges for ordered food items.
"""

bill = float(input("Enter Food Bill: "))

gst = bill * 0.05
service = bill * 0.10
total = bill + gst + service

print("GST =", gst)
print("Service Charge =", service)
print("Total Bill =", total)
