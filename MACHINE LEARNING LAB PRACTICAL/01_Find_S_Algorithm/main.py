import pandas as pd
import numpy as np

# Sample Training Dataset
data = pd.DataFrame([
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
], columns=['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport'])

print("Training Dataset:")
print(data)

# Separate features and target label
X = np.array(data.iloc[:, :-1])
y = np.array(data.iloc[:, -1])

# Initialize the most specific hypothesis
specific_h = ['0'] * X.shape[1]

# Apply Find-S Algorithm
for i, instance in enumerate(X):
    if y[i] == 'Yes':  # Consider only positive instances
        for j in range(len(specific_h)):
            if specific_h[j] == '0':
                specific_h[j] = instance[j]
            elif specific_h[j] != instance[j]:
                specific_h[j] = '?'

print("\nMost Specific Hypothesis (Find-S):")
print(specific_h)
