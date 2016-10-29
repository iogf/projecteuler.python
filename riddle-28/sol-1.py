import math

def fill_spiral(n):
    spiral = []

    for i in range(1, n ** 2 + 1):
        spiral.append(i)

    return spiral

def is_sqr_p(n):
    sq = math.sqrt(n)

    if sq == math.floor(sq):
        return True
    else:
        return False
        
def calculate_sum(spiral):
    sums = 0
    
    i = 0
    inc = 0

    while i < len(spiral):
        sums += spiral[i]

        if is_sqr_p(i + 1):
            inc += 2

        i += inc
        
    return sums
               
def _28():
    spiral = fill_spiral(1001)

    print "sum", calculate_sum(spiral)
_28()
