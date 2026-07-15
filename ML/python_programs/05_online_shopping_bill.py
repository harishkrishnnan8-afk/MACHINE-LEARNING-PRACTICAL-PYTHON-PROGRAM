"""
Question:
Calculate total bill after applying discounts and GST based on purchase amount.
"""

amount = float(input("Enter Purchase Amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

subtotal = amount - discount
gst = subtotal * 0.18
total = subtotal + gst

print("Discount =", discount)
print("GST =", gst)
print("Final Bill =", total)
