from sympy import *
x,y = symbols('x y')
eq = (x**4 - 5*x**2 + 4 + y**2)**2

''' Following two are one and same'''
pprint(eq.subs(x,1).subs(y,2))
pprint(eq.subs([(x,1),(y,2)]))