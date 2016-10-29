from math import *

def readtxt():
    with open('triangles.txt', 'r') as f:
        matrix = f.read()

    matrix = matrix.split('\r\n')

    del(matrix[-1])
    tmp = []

    for i in matrix:
        tmpx = map(int, i.split(','))

        i = 0
        tmpk = []

        while i < len(tmpx) - 1:
            tmpk.append([tmpx[i], tmpx[i+1]])

            i += 2

        tmp.append(tmpk)
                
    return tmp


def getv(a, b):
    return (b[0] - a[0], b[1] - a[1])

"""
def getsign(n):
    if n >= 0:
        return 1
    elif n < 0:
            return -1
"""
def getangle(u, v):

    return (acos(dotprod(u, v)/(getmodule(u) * getmodule(v)))) * 180/pi

def dotprod(u, v):
    r = 0

    for i, j in zip(u, v):
        r += i * j

    return r

def getmodule(u):
    r = 0

    for i in u:
        r += i ** 2

    return r ** (1.0/2)
    
"""
def tricky(x, y, z):
    mx = max(x, y)
    mi = min(x, y)

    if mi <= z <= mx:
        return True
    else:
        return False
"""
def isin(coord, point):
    v11 = getv(coord[0], coord[1])
    v12 = getv(coord[0], coord[2])

    v1p = getv(coord[0], point)
    
    a11 = getangle(v11, v12)
    a12 = getangle(v11, v1p)
    a13 = getangle(v12, v1p)

    if not (a12 <= a11 and a13 <= a11):
        return False 

    v21 = getv(coord[1], coord[0])
    v22 = getv(coord[1], coord[2])

    v2p = getv(coord[1], point)

    a21 = getangle(v21, v22)
    a22 = getangle(v21, v2p)
    a23 = getangle(v22, v2p)
    
    if not (a22 <= a21 and a23 <= a21):
        return False 

    v31 = getv(coord[2], coord[0])
    v32 = getv(coord[2], coord[1])
    
    v3p = getv(coord[2], point)

    a31 = getangle(v31, v32)
    a32 = getangle(v31, v3p)
    a33 = getangle(v32, v3p)

    if not (a32 <= a31 and a33 <= a31):
        return False 
   
    return True

"""    
def metric(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1]-a[1])**2)**(1.0/2)

def eq(xy1, xy2):
    a = (float(xy2[1])-xy1[1])/(xy2[0]-xy1[0])

    b = xy1[1] - a * xy1[0]

    return (a, b)

def isinline(eqt, point):
    if eqt[0] * point[0] + eqt[1] == point[1]:
        return True
    else:
        return False
"""

def _102():
    matrix = readtxt()
    
    s = 0

    n = 0

    for i in matrix:
        if isin(i, (0, 0)):
            s += 1
        else:
            n += 1

    print 'There are {0} triangles containing the origin and {1} not containing!'.format(s, n)
    
    """
    print isin([(0.5, 4), (-1, -1), (1, -1)], (0, 0))
    
    print isin([(-1, -1), (2, -1), (-1, 2)], (0, 0))

    print isin([(-340,495),(-153,-910),(835,-947)], (0, 0))
    print isin([(-175,41),(-421,-714),(574,-645)], (0, 0))

    print isin([(-547,712),(-352,579),(951,-786)], (0, 0))

    print isin([(419,-864),(-83,650),(-399,171)], (0, 0))
    """

_102()
