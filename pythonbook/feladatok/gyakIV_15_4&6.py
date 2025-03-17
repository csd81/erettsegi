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

sz1 = int(input("Kerem az 1. tort szamlalojat: "))
n1 = int(input("Kerem az 1. tort nevezőjét: "))
sz2 = int(input("Kerem az 2. tort szamlalojat: "))
n2 = int(input("Kerem az 2. tort nevezőjét: "))
print(sz1 , '/' , n1, end ='', sep='')
egyszerusit(sz1 , n1)
print(sz2 , '/' , n2, end ='', sep='')
egyszerusit(sz2 , n2)
szoroz(sz1 , n1 , sz2 , n2)
osszead(sz1 , n1 , sz2 , n2)

