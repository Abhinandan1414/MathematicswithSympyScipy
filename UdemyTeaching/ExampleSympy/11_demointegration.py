from sympy import *
x, y, z, t = symbols('x y z t')
pprint(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))
pprint(integrate(exp(-x), (x, 0, oo)))

'''
Definite Integrals
'''
exp = x/(x**2 + 1)

pprint(integrate( exp, (x, 0, 1 )))