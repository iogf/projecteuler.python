import math

def first(n):
    p = 1
    s = 0

    dig = int(math.log(n, 10) + 1)

    nine = n / (10 ** (dig - 9))
   
    for i in xrange(0, 9):
        r = nine % 10

        p *= r
        s += r

        nine = nine / 10

    if p == 362880:
        if s == 45:
            return True

    return False

def last(n):
    p = 1
    s = 0

    for i in xrange(0, 9):
        r = n % 10
        p *= r
        s += r
        n = n / 10

    if p == 362880:
        if s == 45:
            return True


    return False

def _104():
    a, b = 1, 1

    ind = 2

    while True:
        ind += 1
        tmp = b
        b += a
        a = tmp
        

        if last(b):
            if first(b):
                print ind
                return

_104()

