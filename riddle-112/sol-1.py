def is_asc(n):
    while n:
        x = n % 10
        n = n / 10
        y = n % 10

        if x > y and n:
            return False

    else:
        return True 

def is_desc(n):
    while n:
        x = n % 10
        n = n / 10
        y = n % 10

        if x < y and n:
            return False

    else:
        return True 

def is_bouncy(n):
    if not is_asc(n) and not is_desc(n):
        return True
    else:
        return False

def make_ratio(minc, maxc):
    c = 0

    for i in range(minc, maxc + 1):
        if is_bouncy(i):
            c += 1

    return 100 * c / (maxc - minc)

def find_ratio(ratio):
    c , i = 0, 0

    while True:
        if is_bouncy(i):
            c+= 1

            if (c) * 100.0/i > ratio:
                return tmpi, tmpc

            tmpi, tmpc = i, c

        i += 1

def _112():
    print find_ratio(99)[0]
_112()

