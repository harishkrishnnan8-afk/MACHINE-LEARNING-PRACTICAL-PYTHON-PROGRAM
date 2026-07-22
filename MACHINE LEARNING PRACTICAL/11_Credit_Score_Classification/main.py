import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample Dataset
data = {
    "Income":[25000,50000,45000,60000,35000,80000,70000,30000],
    "Age":[22,35,30,45,28,50,40,24],
    "Loan":[5000,10000,8000,12000,6000,15000,13000,4000],
    "CreditScore":["Low","High","Medium","High","Medium","High","High","Low"]
}

df = pd.DataFrame(data)

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

le = LabelEncoder()
y = le.fit_transform(y)

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.25,random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Predicted Credit Scores:")
print(le.inverse_transform(y_pred))

print("\nAccuracy:")
print(accuracy_score(y_test,y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))
