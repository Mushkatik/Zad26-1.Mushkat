def delit(n):
    d = 2
    nd = 0
    while d*d < n:
        if n%d == 0:
            nd = max(nd, d, n//d)
        d+=1
    if d*d == n:
        nd = max(nd, d)
    return nd
f = open('26.txt')
n = int(f.readline())
masizn, maspovt, masnepovt = [],[],[]
maxd, res2 = 0,0
for s in f:
    x = int(s)
    if x not in masizn: masizn.append(x)
    else: maspovt.append(x)
for i in range(len(masizn)):
    if masizn[i] not in maspovt:
        masnepovt.append(masizn[i])
        if delit(masizn[i]) >= maxd:
            maxd = delit(masizn[i])
            res2 = max(res2, masizn[i])
print(len(masnepovt), res2)
f.close()
