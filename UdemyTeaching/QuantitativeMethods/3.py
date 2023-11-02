'''
Compounding factor calculator
Calculates the compounding factor for various combination of
interest rate and year based on monthly
compoundng
Inputs none
Input data can be edited in the program
'''
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
ax = plt.axes(projection ='3d')
#ax = Axes3D(fig)
X = np.arange(4, 10, 1)
print(X)
Y = np.arange(4, 10, 1)
Z = np.zeros((6,6))
print(Y)
for x in X:
    for y in Y:
        print(x ,'percent ',y,'years ', 'compounding factor: ',(1+x/1200)**(y*12))
        Z[x-4][y-4]= (1+x/1200)**(y*12)
print("Compounding factors in table format")
print(Z)
ax.plot_surface(X,Y,Z)
plt.show()