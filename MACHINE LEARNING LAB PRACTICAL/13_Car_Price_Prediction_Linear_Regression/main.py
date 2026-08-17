import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample Dataset
data = {
    "Year":[2015,2016,2017,2018,2019,2020,2021,2022],
    "Mileage":[80000,70000,60000,50000,40000,30000,20000,10000],
    "Price":[400000,500000,600000,700000,800000,900000,1000000,1100000]
}

df = pd.DataFrame(data)

X = df[["Year","Mileage"]]
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.25,random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Actual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(prediction)

print("\nR2 Score:")
print(r2_score(y_test,prediction))
