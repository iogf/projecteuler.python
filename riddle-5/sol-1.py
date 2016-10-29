import math

def is_prime(n):
    max_fact = int(math.floor(math.sqrt(n)))

    for i in range(2, max_fact + 1):
        if not n % i:
            return False
    else:
        return True

def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n
    
def div_list(list, n):

    tmp = []

    for i in list:
        if i == n:
            continue

        if not i % n:
            tmp.append(i / n)
        else:
            tmp.append(i)

    return tmp
       
def test_fact(list, n):
    for i in list:
        if not i % n:
            return True
    else:
        return False
 
def gcd(list):
    
    d = 2
    
    ngcd = 1

    while len(list) > 0:
        if test_fact(list, d):
            list = div_list(list, d)
            ngcd = ngcd * d
        else:
            d = next_prime(d)

    return ngcd


def _5():
    print gcd(range(2, 21))
    

_5()
        
    
        
