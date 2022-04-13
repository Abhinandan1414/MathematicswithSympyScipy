'''rref.py
• At the price of $ 59, the survey says that 87% would buy it.
• At the price of $ 79, the survey says that 61% would buy it.
• At the price of $ 99, the survey says that 42% would buy it.
Every quadratic function can be written in the form
f (x) = ax**2 + bx + c
so
a(59)**2 + b(59) + c = 0.87
a(79)**2 + b(79) + c = 0.61
a(99)**2 + b(99) + c = 0.42
'''

from sympy import *
M = Matrix([[59**2, 59, 1, 0.87], [79**2, 79, 1, 0.61],
           [99**2, 99, 1, 0.42]])
print('The given matrix is {0}'.format(M))
print('The RREF for the same is {0}'.format(M.rref()))
