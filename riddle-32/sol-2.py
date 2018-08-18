# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from itertools import permutations

perms = permutations('123456789', 9)
perms = (''.join(ind) for ind in perms)

prods = ((indi[:indj], indi[indj:indz], indi[indz:])
for indi in perms 
    for indj in range(1, len(indi)) 
        for indz in range(indj + 1, len(indi)))

prods = ((int(''.join(ind[0])), int(''.join(ind[1])), 
int(''.join(ind[2]))) for ind in prods)

prods = filter(lambda ind: ind[0] * ind[1] == ind[2], prods)
prods = map(lambda ind: ind[2], prods)
prods = set(prods)
print(prods)
print('The sum:', sum(prods))
