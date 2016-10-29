
max_sum = 0

listr = []

def sum_pa(n, a_1, r):
    return n * ((a_1 + (n-1)*r) + a_1)/2
    
def indt(cells, i, j):

    ind = sum_pa(i, 1, 1)
    ind += j

    if ind >= len(cells):
        return None
    else:    
        return cells[ind]


def neighbors(cells, i, j):

    retx = indt(cells, i + 1, j)
    rety = indt(cells, i + 1, j + 1)

    if not retx is None:
        listn = [retx]
        listn.append(rety)
        return listn
    else:
        return None

def neighbors_ij(cells, i, j):
    listn = []

    indl = sum_pa(i + 1, 1, 1)
    indl += j


    if indl >= len(cells):
        return None
    else:
        listn.append([i + 1, j])
        listn.append([i + 1, j + 1])
        return listn
   

def findr(cells, i, j, sumr):
    
    listn = neighbors_ij(cells, i, j)
    cell = indt(cells, i, j)

    if listn is None:
        listr.append(sumr + cell)
        return None

 
    findr(cells, listn[0][0], listn[0][1], sumr + cell)
    findr(cells, listn[1][0], listn[1][1], sumr + cell)

def _18():

    data = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    matrix = map(int, data.split(' '))
 
    #print indt(matrix, 15, 0)
    #print sum_pa(3, 1, 1)

 
    findr(matrix, 0, 0, 0)
    listr.sort()

    print listr
    #print neighbors_ij(matrix, 13, 13)

_18()
