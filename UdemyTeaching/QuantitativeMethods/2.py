'''
Compounding factor calculator
Calculates the compounding factor for various combination of
interest rate and year based on yearly
compoundng
Inputs none
Input data can be edited in the program
'''
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
ax = plt.axes(projection='3d')
X = np.arange(4, 10, 1)
print(X)
Y = np.arange(4, 10, 1)
Z = np.zeros((6, 6))
print(Y)
for x in X:
    for y in Y:
        #print(x, y)
        print(x, 'percent ', y, 'years ', (1+x/100)**y)
        Z[x-4][y-4] = (1+x/100)**y
print(Z)
#plt.plot(X,Y,Z)
ax.plot_surface(X, Y, Z)
plt.show()

