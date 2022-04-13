'''
Verify the accuracy of binomial library function with value
derived from first priciples
'''


from sympy import FiniteSet
import random
from scipy.stats import binom
def findProb():
    coinSides = FiniteSet(0,1)
    maxTosses = 5
    successlist = []
    # sample space
    s = coinSides**maxTosses
    for elem in s:
        print(elem)
        if sum(elem) == 4:
            print('success')
            successlist.append(elem)
    e = FiniteSet(*successlist)
    print('Event space',e)
    print('Sample space',s)
    return len(e)/len(s)
if __name__ == '__main__':
    p = findProb()
    print('Probability from basic principles: ',p)
    n = 5
    r = 4
    p = 0.5
    print('Probability with the help of library function:',binom.pmf(r,n,p))