




import sympy


spiral = {}

for n in xrange(2, 10000):
    x = sympy.divisors(n)
    del x[-1]
    a = sum(x)
    spiral[n] = a

result = 0
for n in xrange(2, 10000):
    try:
        d = spiral[n]
    except:
        pass
    else:
        try:
            if spiral[d] == n and n != d:
                result = result + n + d
                del spiral[d]
                del spiral[n]
        except:
            pass
    

print result





