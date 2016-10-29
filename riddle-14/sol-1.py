def collatz(n):
    seq = []

    i = n

    while i > 1:
        seq.append(i)

        if not i % 2: 
            i = i / 2
        else:
            i = 3 * i + 1


    seq.append(1)

    return seq       

def ct_collatz(n):
    i = n

    nterms = 0

    while i > 1:
        if not i % 2: 
            i = i / 2
        else:
            i = 3 * i + 1
        
        nterms += 1


    return nterms + 1

def _14():

    maxp = 0
    

    for i in range(1000001, 0, -1):
        nterm = ct_collatz(i)

        if maxp < nterm: 
            maxp = nterm
            maxi = i

    print maxp, maxi
_14()
