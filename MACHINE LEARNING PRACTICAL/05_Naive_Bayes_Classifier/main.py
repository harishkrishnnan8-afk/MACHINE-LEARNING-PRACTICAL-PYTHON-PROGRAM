import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Encode Categorical Data
le_weather = LabelEncoder()
le_temp = LabelEncoder()

df['Weather'] = le_weather.fit_transform(df['Weather'])
df['Temperature'] = le_temp.fit_transform(df['Temperature'])

X = df[['Weather', 'Temperature']]
y = df['Play']

# Train Model
model = GaussianNB()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

print("Actual Targets:", y.values)
print("Predicted Targets:", y_pred)
print("\nAccuracy Score:", accuracy_score(y, y_pred))
