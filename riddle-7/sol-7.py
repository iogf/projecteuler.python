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

def _7():
    p = 2

    for i in range(0, 10000):
        p = next_prime(p)

    print p

_7()
