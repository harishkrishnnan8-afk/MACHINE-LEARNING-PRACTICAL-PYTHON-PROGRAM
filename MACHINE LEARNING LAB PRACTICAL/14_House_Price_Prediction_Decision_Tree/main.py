import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Sample Dataset
data = {
    "Area":[1000,1200,1500,1800,2000,2200,2500,3000],
    "Bedrooms":[2,2,3,3,4,4,4,5],
    "Price":[3000000,3500000,4500000,5000000,
             6000000,6500000,7500000,9000000]
}

df = pd.DataFrame(data)

X = df[["Area","Bedrooms"]]
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.25,random_state=42
)

model = DecisionTreeRegressor(random_state=42)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(prediction)

print("\nMean Squared Error:")
print(mean_squared_error(y_test,prediction))
