import math

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

def fact(n):
    setd = []

    d = 2

    pw = 0
    flag = False

    while n > 1:
        if not n % d:
            pw += 1
            n = n / d
            flag = True
        else:
            d = next_prime(d)

            if flag:
                setd.append(pw)
                pw = 0  
                flag = False

    setd.append(pw)
    return setd

def t_number(n):
    return n * ( n + 1 ) / 2


def count_facts(npr):
    ft = fact(npr)

    rs = 1

    for i in ft:
        rs = rs * (i + 1)        

    return rs

def count_facts1(npr):
    facts = 0
    maxd = npr/2 + 1

    i = 2

    while i <= maxd:
        if not npr % i:
            facts += count_facts(npr / i)
            facts += 1
            maxd = npr / i
        i +=1

    return facts + 1

def _12():
    i = 1

    #print fact(108)

    #print count_facts(28)

    while True:
        tn = t_number(i)
        #print tn
        cf = count_facts(tn)

        if cf >= 500:
            print tn
            break

        i += 1
    
_12()
