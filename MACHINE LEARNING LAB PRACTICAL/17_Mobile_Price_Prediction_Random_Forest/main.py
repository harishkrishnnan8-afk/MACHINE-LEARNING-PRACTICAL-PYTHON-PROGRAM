import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "RAM":[2,3,4,6,8,12,16],
    "Storage":[32,64,64,128,128,256,512],
    "Battery":[3000,3500,4000,4500,5000,6000,7000],
    "Price":[8000,12000,15000,22000,30000,45000,70000]
}

df = pd.DataFrame(data)

X = df[["RAM","Storage","Battery"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

model = RandomForestRegressor(random_state=42)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(prediction)

print("\nR2 Score:")
print(r2_score(y_test,prediction))
