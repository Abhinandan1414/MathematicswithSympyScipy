'''
Do P and P complement add up to 1?
Let us investigate
'''
import sympy
from sympy import FiniteSet
def probability(space, event):
    return len(event)/len(space)
def greaterThanFive(number):
    if number > 5:
        return True
    else:
        return False
def lessThanOrEqualToFive(number):
    if number <= 5:
        return True
    else:
        return False
if __name__ == '__main__':
    print(__doc__)
    space = FiniteSet(*range(1, 21))
    sixAndAbove = []
    fiveOrLess = []
    for num in space:
        if greaterThanFive(num):
            sixAndAbove.append(num)
    event= FiniteSet(*sixAndAbove)
    p = probability(space, event)
    for num in space:
        if lessThanOrEqualToFive(num):
            fiveOrLess.append(num)
    eventComplement = FiniteSet(*fiveOrLess)
    pComplement = probability(space, eventComplement)
    print('Sample space: ',space)
    print('Events: ',sixAndAbove)
    print('EventComplement',fiveOrLess)
    print('Probability of Dice face being greater than 5: ',p)
    print('Probability of Dice face being 5 or less',pComplement)
    if ( p+pComplement == 1.0):
        print('Law of probability holds good')
    else:
        print('Things are incorrect')