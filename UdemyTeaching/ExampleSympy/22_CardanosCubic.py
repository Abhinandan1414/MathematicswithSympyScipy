from sympy import *

x = Symbol('x')
a = Symbol('a ')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = a*x**3 + b*x**2 + c*x + d 

print("{}".format(solve(e,x)))
pprint(solve(e,x))