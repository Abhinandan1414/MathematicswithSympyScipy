from sympy import *
'''
X**2 = -1
and
X**4 = -1
'''
x = Symbol('x')

f = x**2+1

print("printing for x**2+1")
pprint(solve(f,x))

f = x**4+1

print("printing for x**4+1")
pprint(solve(f,x))

'''
Try for higher power let us say 8
'''