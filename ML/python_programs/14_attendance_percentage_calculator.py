"""
Question:
Calculate attendance percentage and determine examination eligibility (minimum 75%).
"""

total = int(input("Total Classes: "))
attended = int(input("Classes Attended: "))

percentage = (attended / total) * 100

print("Attendance =", percentage, "%")

if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible")
