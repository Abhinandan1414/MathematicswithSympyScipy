'''rref.py
2x − 5z + y =  6+ w
5+ z − y = 0
w + 3(x + y) = z
1 + 2x – y = w − 3x

-w + 2x + y-5z = 6
0w +0x -y + z= -5
w +3x +3y -z = 0
-w + 5x -y + 0z=-1

The Matrix.rref should give the Reduced Row Eichelon Form and 
second is a tuple of indices of the pivot columns.
'''

from sympy import *
M = Matrix([[-1, 2, 1, -5, 6], [0, 0, -1, 1, -5],
           [1, 3, 3, -1, 0], [-1, 5, -1, 0, -1]])
print('The given matrix is {0}'.format(M))
print('The RREF for the same is {0}'.format(M.rref()))
