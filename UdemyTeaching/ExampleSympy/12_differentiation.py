from sympy import *
x, y, z = symbols('x y z')
expr = exp(x*y*z)
pprint(diff(expr,x))
pprint(diff(expr,y))

print("Second order")
pprint(diff(expr,x,x))

print("Second order")
pprint(diff(expr,x,x,x))