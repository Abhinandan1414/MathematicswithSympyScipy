'''
To solve single variable expressions
1. Create symbols
2. Create Expression 
3. Solve the Expression with respect to variables defined
'''
from sympy import *
x = Symbol('x')
print("Given equation is x**2+3*x+2 = 0")
e = x**2 + 3*x + 2
print("Solving the given expression with respect to x {0}".format(solve(e,x)))