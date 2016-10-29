def is_int(n):
    if int(n) == n:
        return True
    else:
        return False


def pytagorean(b):
    c = -(2*(b ** 2)  - 2000*b + 1000000)/(2*b - 2000.0)
    return c

def _9():
    b = 1

    while b < 1000000:
        c = pytagorean(b)
        a = 1000 - c - b 

        if a ** 2 + b ** 2 == c ** 2:
            if a < b and b < c:
                if is_int(a) and is_int(b) and is_int(c):
                    print 'found', a, b, c, a ** 2 + b** 2 , '=', c ** 2
                    print 'product:', a, b, c, '=', a * b * c, 'sum:', a+b+c
                    break
    
        print a + b + c, a, b, c, '-', a**2 + b**2 , '=', c**2
        
        b += 1
        
_9()
