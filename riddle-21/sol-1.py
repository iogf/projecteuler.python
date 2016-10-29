import sympy
import math

list_primes = []

def generate_list_primes(n):
    np = 2

    while np < n:
        list_primes.append(np)
        np = next_prime(np)


def next_prime(n):
    i = n + 1

    while not sympy.isprime(i):
        i += 1
   
    return i

def sum_d(n):
    divs = sympy.divisors(n)

    sumd = 0

    for i in divs[:-1]:
        sumd += i

    return sumd
            

def test_common_factor(a, b):
    
    maxa = int(math.sqrt(a))
    maxb = int(math.sqrt(b))
    i = 0

    f = list_primes[0]

    while f <= maxa and f <= maxb:
        if not a % f and not b % f:
              return True
        
        i += 1
        f = list_primes[i]

    else:
        return False

    
def is_amicable(a, b):

    if test_common_factor(a, b):
        if sum_d(a) == b and sum_d(b) == a:
            return True
        else:
            return False
    else:
        return False


def _21():
    suma = 0
    generate_list_primes(10001)

    #print test_common_factor(5, 20)

    
    
    for i in range(2, 10001):
        for j in range(i + 1, i + 999): # 999 is a epslon for b - a < 999 for all b, a amicable and lesser than 10001
            if is_amicable(i, j):
                print i, j
                suma += i + j

    print suma

_21()
