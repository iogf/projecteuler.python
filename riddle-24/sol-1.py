import itertools

def tonumb(tupla):
    numb = ''

    for i in tupla:
        numb += i

    return int(numb)

def _25():
    pmt = itertools.permutations('0123456789', 10)

    lexic = [x for x in pmt if tonumb(x)]

    lexic_numb = map(tonumb, lexic)
    lexic_numb.sort()

    print lexic_numb[999999] 

_25()
