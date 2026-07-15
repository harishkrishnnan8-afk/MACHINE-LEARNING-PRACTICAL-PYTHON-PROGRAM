"""
Question:
Calculate Body Mass Index (BMI) and classify the patient's health status.
"""

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height * height)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("BMI =", round(bmi, 2))
print("Status =", status)
