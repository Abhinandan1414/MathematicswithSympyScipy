import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ax = plt.axes(projection='3d')


x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55,34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)
x1 = x[...,0]
x2 = x[...,1]
print(x)
print(y)
print(x1)
print(x2)
ax.plot3D(x1, x2, y, 'gray')
model = LinearRegression().fit(x, y)
modelscore = model.score(x, y)
print('slope:', model.coef_)
print('r_squared:',modelscore)
print('intercept:', model.intercept_)
y_pred = model.predict(x)
ax.plot3D(x1, x2, y, 'red')
ax.plot3D(x1, x2, y_pred, 'blue')
print('predicted response:', y_pred, sep='\n')
plt.show()