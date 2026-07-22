from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split Dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=0
)

# Train Model
model = GaussianNB()

model.fit(X_train,y_train)

# Prediction
prediction = model.predict(X_test)

print("Predicted Classes:")
print(prediction)

print("\nAccuracy:")
print(accuracy_score(y_test,prediction))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,prediction))

print("\nClassification Report:")
print(classification_report(y_test,prediction))
