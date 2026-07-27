import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

# Sample Dataset
data = pd.DataFrame([
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
], columns=['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

# Encode categorical variables
df_encoded = data.copy()
for col in df_encoded.columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])

X = df_encoded.iloc[:, :-1]
y = df_encoded.iloc[:, -1]

# Train Decision Tree using entropy (ID3)
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, y)

print("Decision Tree Rules (ID3):")
print(export_text(clf, feature_names=list(X.columns)))
