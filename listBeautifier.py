def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        _, *res, _ = res
    return res

a = [3, 4, 2, 4, 38, 4, 5, 3, 2]
listBeautifier(a)