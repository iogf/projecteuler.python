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

def _10():
    sum = 0

    p = 2

    while p < 2000000:
        sum += p
        p = next_prime(p)


    print sum
_10()
