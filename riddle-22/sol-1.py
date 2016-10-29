def alpha():
    f = open('names.txt', 'r')
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
        
def _22():
    txt = alpha()
    sum_scory = 0
    for i in range(0, len(txt)): 
        sum_scory += get_scory(txt[i]) * (i + 1)
    print sum_scory

_22()

