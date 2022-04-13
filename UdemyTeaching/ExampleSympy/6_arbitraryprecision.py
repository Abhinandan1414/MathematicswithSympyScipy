#!/usr/bin/env python
"""Precision Example
Demonstrates SymPy's arbitrary integer precision abilities
Prepared with the help of Sympy Documentation
"""
import sympy
from sympy import Mul, Pow, S, pprint
def main():
    print(__doc__)
    x = Pow(2, 50, evaluate=False)
    y = Pow(10, -50, evaluate=False)
    # A large, unevaluated expression
    m = Mul(x, y, evaluate=False)
    # Evaluating the expression
    print('Value of Expression')
    e = S(2)**50/S(10)**50
    pprint(m)
    print('is as follows:')
    print(e)
if __name__ == "__main__":
    main()