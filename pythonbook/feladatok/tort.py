import sys

def egesz_e(sz,n):
    if sz % n == 0:
        print(int(sz/n))
    else:
        print("Nem egész!")    

def lnko(a,b):
    if a==b:
        return a
    elif a<b:
        return lnko(a,b-a)
    else:
        return lnko(a-b,a)
    
def lkkt(a,b):
    return a*b/lnko(a,b)

def szoroz(sz1,n1,sz2,n2):
    esz,en = sz1*sz2,n1*n2
    if esz % en == 0:
        print("%d/%d * %d/%d = %d/%d = %d" % \
              (sz1,n1,sz2,n2,esz,en,esz/en))
    else:
        print ("%d/%d * %d/%d = %d/%d = %d/%d" % \
               (sz1,n1,sz2,n2,esz,en,esz/lnko(esz,en),en/lnko(esz,en)))

def osszead(sz1,n1,sz2,n2):
    en = lkkt(n1,n2)
    bsz1,bsz2 = sz1*en/n1,sz2*en/n2
    esz=bsz1+bsz2
    if esz % en == 0:
        print("%d/%d + %d/%d = %d/%d + %d/%d = %d/%d = %d" % \
              (sz1,n1,sz2,n2,bsz1,en,bsz2,en,esz,en,esz/en))
    else:
        print ("%d/%d + %d/%d = %d/%d + %d/%d = %d/%d = %d/%d" % \
                (sz1,n1,sz2,n2,bsz1,en,bsz2,en,esz,en, \
                 esz/lnko(esz,en),en/lnko(esz,en)))
    
print("1. feladat")
print ("Számláló:")
szaml1 = int(input())
print ("Nevező:")
nev1 = int(input())
egesz_e(szaml1,nev1)
print("3. feladat")
print ("%d/%d = %d/%d" % \
       (szaml1,nev1,szaml1/lnko(szaml1,nev1),nev1/lnko(szaml1,nev1)))
print("4. feladat")
print ("2. tört számláló:")
szaml2 = int(input())
print ("2. tört nevező:")
nev2 = int(input())
szoroz(szaml1,nev1,szaml2,nev2)
print("6. feladat")
osszead(szaml1,nev1,szaml2,nev2)
print("7. feladat")
be = open("adat.txt",'r')
regi_kimenet=sys.stdout
ki=open("eredmeny.txt",'w')
sys.stdout=ki
line = be.readline()
while line!="":
    valt = line.split()
    szaml1,nev1, szaml2, nev2 = \
                 int(valt[0]), int(valt[1]),int(valt[2]), int(valt[3])
    if valt[4]=="*":
        szoroz(szaml1,nev1,szaml2,nev2)
    else:
        osszead(szaml1,nev1,szaml2,nev2)
    line=be.readline()
be.close()
sys.stdout=regi_kimenet
ki.close()
