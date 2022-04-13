#!/usr/bin/env python
"""Functions example
Demonstrates functions defined in SymPy.
Prepared with help of Sympy documentation
"""
from sympy import pprint, Symbol, log, exp
def main():
    print(__doc__)
    a = Symbol('a')
    b = Symbol('b')
    e = log((a + b)**5)
    print('Constructed expression is')
    pprint(e)
    print('\n')
    print(' e raise to the expression is')
    e = exp(e)
    pprint(e)
    print('\n')
    print('Another constructed expression is')
    e = log(exp((a + b)**5))
    pprint(e)
    print
if __name__ == "__main__":
 main()
