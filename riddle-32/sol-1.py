import itertools

def xyz(obj):
    listx = []

    for i in range(1, len(obj)):
        for j in range(i + 1, len(obj)):
            listx.append((obj[0:i], obj[i:j], obj[j:]))
                
    return listx

def simplify(obj):
    listx = []

    for i in obj:
        ndigx = len(i[0])
        ndigy = len(i[1])
        ndigz = len(i[2])

        ndigs = ndigx + ndigy
        
        if ndigs != ndigz:
            #if ndigs != ndigz - 1:
            if ndigs - 1 != ndigz:
                continue

        listx.append(i)

    return listx
      
def criterea(eq):
    x = int(eq[0])
    y = int(eq[1])
    z = int(eq[2])

    if x * y == z:
        return True
    else:
        return False

def tostr(obj):
    s = ''
    for i in obj:
        s += i

    return s
    

def tetha(listx):
    listall = []

    for i in listx:
        listall += xyz(i)

    return listall
   

def third_field(listx):
    listp = set()

    for i in listx:
        listp.add(i[2])
        
    return listp

def prod(listx):
    result = 0

    for i in listx:
        result += int(i)

    return result

def _32():
    digs = '123456789'

    listx = [ x for x in itertools.permutations(digs, 9)]

    listx = map(tostr, listx)

    listx = tetha(listx)

    listx = simplify(listx)

    listx = filter(criterea, listx)
    
    print listx

    listx = third_field(listx)

    print listx
    print "Product:", prod(listx)    

_32()
