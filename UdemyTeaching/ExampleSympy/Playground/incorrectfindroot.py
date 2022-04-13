'''
find_root( 7000 == 5000*(1+0.045/12)^n)
'''

from sympy import *

n = Symbol("n")
eq = 7000 - (5000 * (1 +0.045/12)**n)
print(solve(eq,n))
