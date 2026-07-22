import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dataset
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([1,4,9,16,25,36,49,64,81,100])

# Linear Regression
linear = LinearRegression()
linear.fit(X,y)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly,y)

# Prediction
linear_pred = linear.predict(X)
poly_pred = poly_model.predict(X_poly)

# Plot
plt.scatter(X,y,color='red')
plt.plot(X,linear_pred,color='blue',label='Linear')
plt.plot(X,poly_pred,color='green',label='Polynomial')
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("Linear Regression Score:",linear.score(X,y))
print("Polynomial Regression Score:",poly_model.score(X_poly,y))
