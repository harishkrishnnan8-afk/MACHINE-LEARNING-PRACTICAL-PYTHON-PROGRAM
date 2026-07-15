"""
Question:
Accept marks of five subjects, calculate total, average, and assign grades (A, B, C, etc.).
"""

marks = []
for i in range(5):
    marks.append(float(input("Enter Mark: ")))

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Total =", total)
print("Average =", average)
print("Grade =", grade)
