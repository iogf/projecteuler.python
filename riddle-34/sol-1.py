import math

def fact(n):
    prod = 1

    for i in range(1, n+1):
        prod *= i

    return prod

def sum_of_facts_for_digits(n):
    sumf = 0
    
    ns = str(n)

    for i in ns:
        sumf += fact(int(i))

    return sumf

def find_limit():
    pot = 1

    while True:
        next = 10 ** pot - 1
        rets = sum_of_facts_for_digits(next) 

        if next > rets:
            break 

        pot += 1

    return 10 ** (pot - 1) - 1
        
def _34():
    #print sum_of_facts_for_digits(145)

    maxn = find_limit()
    listf = []

  
    sumf = 0

    for i in range(3, maxn):
        if sum_of_facts_for_digits(i) == i:
            sumf += i
            listf.append(i)

    print sumf

_34()

