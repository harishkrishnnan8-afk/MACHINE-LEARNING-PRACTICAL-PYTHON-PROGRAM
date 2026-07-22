from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=1
)

model = Perceptron(max_iter=1000)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Accuracy:")
print(accuracy_score(y_test,prediction))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,prediction))
