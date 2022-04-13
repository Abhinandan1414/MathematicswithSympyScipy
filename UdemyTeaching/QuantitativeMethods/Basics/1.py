'''
PythaGoras.py
Calculate the distance between points (x1,y1) and (x2,y2)
'''
import math
from fractions import Fraction
if __name__=='__main__':
    print(__doc__)
    try:
        x1 = Fraction(input('Enter Fraction x1 of first point '))
        y1 = Fraction(input('Enter Fraction y1 of first point '))
        x2 = Fraction(input('Enter Fraction x2 of second point '))
        y2 = Fraction(input('Enter Fraction y2 of second point '))
        result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print('The Distance between point {0},{1} and {2},{3} is {4}'.format(x1,y1,x2,y2,result))
    except ValueError:
        print('Incorrect fractions entered')
