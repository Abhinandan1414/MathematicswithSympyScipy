# A Python program to print all
# permutations using library function
from itertools import permutations
from itertools import combinations

# Get all permutations of [1, 2, 3]
perm = permutations(['ace', 'king', 'queen','jack'])

# Print the obtained permutations
for i in list(perm):
	print (i)


print("Now printing all combinations with 3 cards taken at a time")

comb = combinations(['ace', 'king', 'queen','jack'], 3)
for i in list(comb):
    	print (i)

