'''
Example to show how to plot given:
Revenue
Cost
and therefore
profit functions graphically for further inference

The ice cream vendor observes that when he charges $ 3 per ice cream
cone, he only sells 120 cones per day. On the other hand, when he charges
$ 2 per ice cream cone, he sells 200 cones per day. In our example, because
he has long since paid off his start-up expenses, the costs of doing business
are just 50 cents per cone, plus a $ 100 per day fee for his permit to sell
food in Central Park. As you might imagine, if he makes his price too high,
he will sell too few cones, and won’t make much profit; if he makes his price
too low, he will sell more cones, but he still won’t make much profit.
The ice cream vendor is going to assume that the demand varies linearly
with price. This often is not quite true, but it is often a reasonable approx-
imation. There are several different ways to realize that the demand n, and
the price p, will have the relationship

Given:
At $3 price demand was 120
At $2 price demand was 200

//Inference:
Means every dollar decrease increases demand by 80 units
Extrapolating linearly:
At $1 price demand will be 280
At $0 price demand will be 360
On the other side, the demand
At $4 price demand will be 40
At $4.5 price demand will be 0

Big assumption is LINEAR.

n = 360 - 80p
or equivalently
p = 4.50 - n/80

r(n) = n*p = n (4.50-n/80) 

c(n) = 0.50n + 100

'''
import matplotlib.pyplot as plt
import math
def revenue(unitsSold):
 return 4.5*unitsSold - ((unitsSold ** 2)/80)
def cost(unitsSold):
 return 0.5*unitsSold + 100
def profit(unitsSold):
 return revenue(unitsSold)-cost(unitsSold)
if __name__ == '__main__':
 # assume values of x
    print(__doc__)
    unitValues = range(0, 350, 1)
    revenueValues = []
    costValues = []
    profitValues = []


    for x in unitValues:
    # calculate the values of the y as list
        revenueValues.append(revenue(x))
        costValues.append(cost(x))
        profitValues.append(profit(x))
    plt.plot(unitValues,revenueValues,'-',label='revenue')
    plt.plot(unitValues,costValues,'.', label = 'cost')
    plt.plot(unitValues,profitValues,':',label = 'profit')
    plt.legend()
    plt.title("revenue cost profit")
    plt.show()