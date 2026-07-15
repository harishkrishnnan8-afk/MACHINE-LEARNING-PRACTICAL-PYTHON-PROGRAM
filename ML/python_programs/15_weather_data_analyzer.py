"""
Question:
Store daily temperatures for a week and find maximum, minimum, and average temperature.
"""

temp = []

for i in range(7):
    temp.append(float(input("Enter Temperature: ")))

print("Maximum =", max(temp))
print("Minimum =", min(temp))
print("Average =", sum(temp) / 7)
