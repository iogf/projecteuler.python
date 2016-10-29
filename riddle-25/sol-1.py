import math

def next_fib(a, b):
    return a + b

def fib(n):
    a, b = 1, 1

    if n <= 2:
        return 1

    for i in range(2, n):
        tmp = b
        b = a + b
        a = tmp
        
    return b

def _25():
    a = 1
    b = 1

    i = 2

    while True:
        digits = int(math.log(b, 10)) + 1
     
        if digits >= 1000:
            break

        tmp = b
        b = next_fib(a, b)
        a = tmp
        i += 1
    
    print i

_25()

