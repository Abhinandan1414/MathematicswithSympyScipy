#!/usr/bin/env python
"""Substitution example
Demonstrates substitution.
"""
import sympy
from sympy import pprint, cos, Float, Symbol, log
def main():
    x = Symbol('x')
    y = Symbol('y')
    print('Let us start with')
    e = 1/cos(x)
    print()
    pprint(e)
    print('\n')


    print('Let us substitute cos(x) with y')
    pprint(e.subs(cos(x), y))
    print('\n')
    print('Let us substitute y with x square')
    pprint(e.subs(cos(x), y).subs(y, x**2)) #Watch the cascading of subs
    e = 1/log(x)
    print('Given expression')
    pprint(e)
    print('Substitute 2.71828 for x')
    e = e.subs(x, sympy.Float("2.71828"))
    print('\n')
    print('Evaluated expression is ')
    pprint(e.evalf())
    print()
    print('Let us construct following expression')
    a = Symbol('a')
    b = Symbol('b')
    e = a*2 + a**b/a
    print('\n')
    pprint(e)
    print('Substitute a with 8')
    print('\n')
    pprint(e.subs(a,8))
    print()
if __name__ == "__main__":
    main()
