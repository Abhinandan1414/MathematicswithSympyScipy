'''
EmiFactor calculator
Accepts user input parameters none
Emits tabular EmiFactor for various combination of interest rate
and period
Calculations are monthly
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def emiFactor(interest,period):
    return ((interest/1200)*(1+interest/1200) ** (period*12))/((1+interest/1200) ** (period*12) -1)
print(__doc__)
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(4, 10, 1) # Interest rate in percentage
print(X)
Y = np.arange(4, 10, 1) # Number of years
Z = np.zeros((6,6))
print(Y)
for x in X:
    for y in Y:
        print(x,y)
        print(x ,'percent ',y,'years ', emiFactor(x,y))
        Z[x-4][y-4]= emiFactor(x,y)
print(Z)
#plt.plot(X,Y,Z)
ax.plot_surface(X,Y,Z)
plt.show()
