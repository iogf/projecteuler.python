

def cmb(x, y):
    seq = []

    for i in range(x[0], x[1] + 1):
        for j in range(y[0], y[1] + 1):
            if not i ** j in seq :
                    seq.append(i ** j)

    return seq
            
def _29():
    
    seq = cmb([2, 100], [2, 100])
    seq.sort()
    print len(seq)


_29()
