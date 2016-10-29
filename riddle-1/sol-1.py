def s(n, a):
    sum = 0

    for i in range(1, n):
        if not i % a:
            sum += i

    return sum


print s(1000, 3) + s(1000, 5)


# import vyapp.plugins.pdb.debug
# load(vyapp.plugins.pdb.debug)

