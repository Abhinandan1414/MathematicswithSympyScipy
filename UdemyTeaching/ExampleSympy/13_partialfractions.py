from sympy import *
x = Symbol('x')
eq = (1+3*x)/(x**2+5*x+6)
pprint(apart(eq))

print()
print('====================')
eq = (x**3-x)/(x**2+5*x+6)
pprint(apart(eq))

print()
print('====================')
eq = (x**2 + 2*x + 1)/(x**2 + x)
pprint(cancel(eq))



