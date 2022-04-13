''' Simple Linear Regression with Linear Data'''
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 35, 55, 75, 95, 115])
print(x)
print(y)
model = LinearRegression().fit(x, y)
modelscore = model.score(x, y)
plt.plot(x,y,'--k')
plt.plot(x, y, 'ok', ms=10)
plt.show()
print('model score:',modelscore)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
