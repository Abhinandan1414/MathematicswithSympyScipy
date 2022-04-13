from sympy import *
x,y = symbols('x y')

print()
print('====================')
eq1 = sin (x + y)
eq2 = tan (2*x)
pprint(expand_trig(eq1))

print('====================')
pprint(expand_trig(eq2))