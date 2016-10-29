def istr(n):
    c = 2 * n

    delta = 1 + (-4)*(-c)

    x1 = (-1 + delta ** (1/2.0))/2
    x2 = (-1 - delta ** (1/2.0))/2

    x = max(x1, x2)

    if int(x) == x:
        return True
    else:
        return False
    
    
def alpha():
    f = open('words.txt', 'r')
    txt = f.read()

    txt = txt.replace('"', '')
    txt = txt.replace('\n', '')
    txt = txt.split(',')

    txt.sort()

    return txt

def get_scory(word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    scory = 0

    for i in word:
        scory += alphabet.find(i) + 1

    return scory

def iswordtr(word):
    scory = get_scory(word)

    if istr(scory):
        return True
    else:
        return False

def count(txt):
    c = 0

    for i in txt:
        if iswordtr(i):
            c+=1

    return c

def _42():

    txt = alpha()

    print count(txt)

_42()
