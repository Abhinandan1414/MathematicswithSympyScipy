'''
Break even point calculator for given fixed cost and variable
cost
Enter the required values from the prompt
Ex: Maximum units sold -> 1000
Fixed cost -> 1000
Variable cost per unit -> 5

Developing a model is an important part of the quantitative analysis approach. Let’s see how we
can use the following mathematical model, which represents profit:
Profit = Revenue - Expenses
Profit = Revenue - (Fixed cost + Variable cost)
Profit = (Selling price per unit)(Number of units sold)
- [Fixed cost + (Variable cost per unit)(Number of units sold)]
Profit = SX - [F + VX]
Profit = SX - F - VX
at Break Even Profit is Zero (0)
Therefore break even point Xb = F/(S-X)

'''
import matplotlib.pyplot as plt
if __name__ == '__main__':
 # assume values of x
   print(__doc__)
   print('Enter the maximum units sold')
   maximumUnitsSold = int(input())
   print('Enter fixed cost')
   fixedCost = int(input())
   print('Enter the variable cost per unit')
   variableCostPerUnit = int(input())
   print('Enter the selling price per unit')
   sellingPrice = int(input())
   x_values = range(0, maximumUnitsSold, 1)
   y_values = []
   for x in x_values:
   # calculate the values of the y as list
      y_values.append(sellingPrice*x - variableCostPerUnit*x - fixedCost)
   breakEvenPoint = int(fixedCost/(sellingPrice - variableCostPerUnit))
   stringBreakEvenPoint = str(breakEvenPoint)
   print('The business breaks even at',breakEvenPoint,'units')
   plt.plot(x_values,y_values)
   plotTitle = "The buisness breaks even at "+stringBreakEvenPoint+" units"
   plt.title(plotTitle)
   plt.ylabel('Profit')
   plt.show()