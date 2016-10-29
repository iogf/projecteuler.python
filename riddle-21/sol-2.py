
import sympy

result = 0


for n in xrange(2, 10000):
    x = sympy.divisors(n)
    del x[-1]
    a = sum(x)
    x = sympy.divisors(a)
    del x[-1]
    b = sum(x)
    if b == n and a != n:
        result = result + n


print result




