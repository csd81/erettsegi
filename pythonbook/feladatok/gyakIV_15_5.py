def lnko(a, b):
    if a == b:
        return int(a)
    if a < b:
        return lnko(a , b - a)
    if a > b:
        return lnko(a - b , b)

def lkkt(a, b):
    return int(a * b / lnko(a , b))

def egyszerusit(szaml, nev):
    print(" = ", end='')
    if szaml % nev == 0:
        print(int(szaml/nev))
    else:
        print(int(szaml/lnko(szaml,nev)), '/', int(nev/lnko(szaml,nev)), sep='')

def szoroz(szaml1, nev1, szaml2, nev2):
    print(szaml1, '/', nev1, " * ", szaml2, '/', \
          nev2, " = ", szaml1 * szaml2, '/', nev1 * nev2, end='', sep='')
    egyszerusit(szaml1 * szaml2 , nev1 * nev2)

def osszead(szaml1, nev1, szaml2, nev2):
    kn = lkkt(nev1 , nev2)
    bov1 = int(szaml1 * kn / nev1)
    bov2 = int(szaml2 * kn / nev2)
    print(szaml1 , '/' , nev1 , " + " , szaml2 , '/' , nev2
         , " = " , bov1 , '/' , kn , " + " , bov2 , '/' , kn
         , " = " , bov1+bov2 , '/' , kn, end='', sep='')
    egyszerusit(bov1 + bov2 , kn)

print(lnko(6,6))
print(lnko(120,75))
print(lnko(75,120))
print(lkkt(75,120))
egyszerusit(12,15)
egyszerusit(6,2)
szoroz(2,3,3,4)
osszead(1,2,3,4)

