''' Linear Regression with Polynomial Features'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])
print(x)
transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x)
x_ = transformer.transform(x)
print("x_ :",x_)
model = LinearRegression().fit(x_, y)
print(x_[...,1])
plt.plot(x_[...,1],y)
y_pred = model.predict(x_)
plt.plot(x_[...,1],y_pred)
plt.show()
modelscore = model.score(x_, y)
print('modelscore:',modelscore)
print('intercept:', model.intercept_)
print('slope:', model.coef_)