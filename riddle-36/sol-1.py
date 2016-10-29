def is_palin(str):
    i, j = 0, len(str)-1

    while i < j:
        if str[i] == str[j]:
            i += 1
            j -= 1
            continue
        else:
            return False

    return True


def _36():
    i = 1
    sumr = 0
    
    for i in range(1, 1000000):
        if is_palin(str(i)):
            if is_palin(bin(i)[2:]):
                print i
                sumr += i

    print "sum:", sumr        

_36()
