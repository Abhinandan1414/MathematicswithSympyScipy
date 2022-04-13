from sympy import *
'''
x**6 - 21x**5 + 175x**4 - 735x**3 + 1624x**2 - 1764*x + 720 = 0
'''
x = Symbol('x')

e = x**6 - 21*x**5 + 175*x**4 - 735*x**3 + 1624*x**2 - 1764*x + 720

print(solve(e,x))

f = x**8+1

pprint(solve(f,x))