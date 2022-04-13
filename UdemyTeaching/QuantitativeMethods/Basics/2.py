'''
CalCulator_for_Elementary.py
Accepts two fractions and then performs +, -, *, / depending upon
choice
'''
from fractions import Fraction
if __name__ == '__main__':
    print(__doc__)
    while True:
        try:
            a = Fraction(input('Enter first fraction: '))
            b = Fraction(input('Enter second fraction: '))
            op = input('Operation to perform +, -, /, * : ')
            if op == '+':
                print('Result of adding {0} and {1} is {2}'.format(a, b, a+b))
            if op == '-':
                print('Result of subtraction {0} and {1} is {2}'.format(a, b, a-b))
            if op == '*':
                print('Result of multiplying {0} and {1} is {2}'.format(a, b, a*b))
            if op == '/':
                print('Result of dividing {0} and {1} is {2}'.format(a, b, a/b))
        except ValueError:
            print('Invalid fraction entered')
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
