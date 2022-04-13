
from sympy import *
'''
9a + 3b + 1c = 32
4a + 2b + 1c = 15
1a + 1b + 1c = 6
'''
a = Symbol('a ')
b = Symbol('b')
c = Symbol('c')

e = 9*a + 3*b + c - 32
f = 4*a + 2*b + c - 15
g = a + b + c - 6

print(solve([e,f,g],a,b,c))