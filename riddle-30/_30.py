def sum_of_digits(n):
    ns = str(n)
    sumd = 0

    for i in ns:
        sumd += int(i) ** 5

    return sumd

def _30():
    fifth = []

    i = 2
    sumall = 0

    
    maxn = 6 * 9 ** 5

    while i <= maxn:
        if sum_of_digits(i) == i:
            fifth.append(i)
            sumall += i
        i += 1

    print sumall

_30()

