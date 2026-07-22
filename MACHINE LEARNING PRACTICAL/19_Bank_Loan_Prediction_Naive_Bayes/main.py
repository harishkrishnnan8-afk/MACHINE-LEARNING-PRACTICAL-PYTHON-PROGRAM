import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    "Income":[25,40,60,80,35,50,70,90],
    "Age":[22,35,40,50,28,30,45,55],
    "LoanAmount":[5,8,10,15,6,7,12,16],
    "LoanApproved":[0,0,1,1,0,1,1,1]
}

df = pd.DataFrame(data)

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.25,random_state=42
)

model = GaussianNB()

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Predictions:")
print(prediction)

print("\nAccuracy:")
print(accuracy_score(y_test,prediction))
