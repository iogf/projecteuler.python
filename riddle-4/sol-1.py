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

def _4():
    maxp = 0
    f1 = 0
    f2 = 0

    for i in range(1, 1000):
        for j in range(1, 1000):
            prod = i * j

            if is_palin(str(prod)):
                    if maxp < prod:
                        maxp = prod
                        f1 = i
                        f2 = j


    print maxp, f1, f2
_4()

