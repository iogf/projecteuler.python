from itertools import permutations

def is_div(num):
    p0 = int('%s%s%s' % (num[1], num[2], num[3]))
    p1 = int('%s%s%s' % (num[2], num[3], num[4]))
    p2 = int('%s%s%s' % (num[3], num[4], num[5]))
    p3 = int('%s%s%s' % (num[4], num[5], num[6]))
    p4 = int('%s%s%s' % (num[5], num[6], num[7]))
    p5 = int('%s%s%s' % (num[6], num[7], num[8]))
    p6 = int('%s%s%s' % (num[7], num[8], num[9]))

    cond = (p0 % 2 == 0) and (p1 % 3 == 0) and (p2 % 5 == 0) and\
    (p3 % 7 == 0) and (p4 % 11 == 0) and (p5 % 13 == 0) and\
    (p6 % 17 == 0)
    
    if cond: return True
    return False

sum = 0
perms = permutations('0123456789')

for ind in perms:
    if is_div(ind):
        sum = sum + int(''.join(ind))

print('Sum:%s' % sum)
