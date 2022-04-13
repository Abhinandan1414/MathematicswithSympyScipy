from sympy import *

x = Symbol('x')
a = Symbol('a ')
b = Symbol('b')
c = Symbol('c')
d = a*x**2 + b*x + c 
print("{}".format(solve(d,x)))
pprint(solve(d,x))

