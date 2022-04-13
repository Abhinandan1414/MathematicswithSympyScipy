import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

'''
https://education.molssi.org/python-data-analysis/03-data-fitting/index.html is modified for cobalt data
cobalt_data=[ (0, 2000), (0.75, 1414), (1.5, 1000), (2.25, 707),
(3.00, 500), (3.75, 353), (4.50, 250),
 (5.25, 177), (6.00, 125)]
'''
xdata = [ 0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.50, 5.25, 6.0]
ydata = [2000, 1414, 1000, 707, 500, 353, 250, 177, 125]

#Recast xdata and ydata into numpy arrays so we can use their handy features
xdata = np.asarray(xdata)
ydata = np.asarray(ydata)
plt.plot(xdata, ydata, 'o')

# Define the Gaussian function
def model(x, a, b):
    #y = A*np.exp(-1*B*x**2)
    y = a*np.exp(b*x)
    return y

parameters, covariance = curve_fit(model, xdata, ydata)

fit_A = parameters[0]
fit_B = parameters[1]
print(fit_A)
print(fit_B)

fit_y = model(xdata, fit_A, fit_B)
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xdata, fit_y, '-', label='fit')
plt.legend()
plt.show()

SE = np.sqrt(np.diag(covariance))
SE_A = SE[0]
SE_B = SE[1]

print(F'The value of A is {fit_A:.5f} with standard error of {SE_A:.5f}.')
print(F'The value of B is {fit_B:.5f} with standard error of {SE_B:.5f}.')