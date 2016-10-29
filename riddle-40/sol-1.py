import math

def dig(n):
    c = 0

    i = 0

    ln = int(math.log(n, 10))

    while True:
        k = int(math.log(i, 10))
        
        if c + k > n-1:
            return str(i)[(n-c)-1]

        c+=k
            
        i+=1

def digx(n):
    i = 0
    c = 0

    while True:
        ns = str(i)
        c += len(ns)

        if c > n:
            return ns[n-c]

        i += 1

        
def _40():

    prod = 1

    for i in range(1, 7):
        prod *= int(digx(10**i))

    print prod
  
_40()
