import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample Dataset
data = {
    "Month":[1,2,3,4,5,6,7,8,9,10,11,12],
    "Advertising":[20,25,30,35,40,50,60,65,70,75,80,90],
    "Sales":[100,120,130,150,170,200,220,240,260,280,300,330]
}

df = pd.DataFrame(data)

X = df[["Month","Advertising"]]
y = df["Sales"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Actual Sales:")
print(y_test.values)

print("\nPredicted Sales:")
print(prediction)

print("\nMean Squared Error:")
print(mean_squared_error(y_test,prediction))
