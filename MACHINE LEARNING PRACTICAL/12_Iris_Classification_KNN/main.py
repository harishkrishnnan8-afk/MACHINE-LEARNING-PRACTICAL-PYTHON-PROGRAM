from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report

iris = load_iris()

X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=1
)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test,prediction))

print("\nClassification Report:")
print(classification_report(y_test,prediction))

print("\nPredicted Classes:")
print(prediction)
