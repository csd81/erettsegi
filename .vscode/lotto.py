print("\n1. feladat\n")
sor=input("Kérem az 52. hét megadott lottószámait (89 24 34 11 64) szóközökkel elválasztva! ")
darsor=sor.strip().split()


lotto52het=list(map(int,darsor))
print("\n2. feladat\n")
lotto52het.sort()
print("Az 52. hét lottószámai nagyság szerint rendezve: ", end="")
for szam in lotto52het:
 print(szam,end=" ")
print()
print("\n3. feladat\n")
het=int(input("Kérem a vizsgált hét sorszámát 1 és 51 között! "))
print("\n4. feladat\n")
lottok=[]
betxt = open("lottosz.dat")
for i in range(51):
    sor=betxt.readline()
    darsor=sor.strip().split()
    lotto=list(map(int,darsor))
    lottok.append(lotto)
betxt.close()
print(f'A(z) {het}. hét lottószámai : ', end="")

for szam in lottok[het-1]: # az 1. hét számai a lottok[0] listában vannak
    print(szam,end=" ")

print()
print("\n5. feladat\n")
# A lottószámok gyakorisági táblázatának elkészítése
gyak=[]
for i in range(90):
    gyak.append(0) # kezdőértékek

for lotto in lottok:
    for szam in lotto:
        gyak[szam-1]+=1

van=gyak.count(0)>0
if van:
    kinemhuzottak=list(filter(lambda i: gyak[i-1]==0,range(1,91))) # szorgalmi feladat
    print(f'Van. (Összesen {gyak.count(0)} db: {kinemhuzottak})')
else:
    print("Nincs.")

print("\n6. feladat\n")

# a)
db=0
for i in range(0,90,2): # csak a páratlan számokat nézzük, pl. gyak[10] a 11 gyakorisága
    db+=gyak[i]

print(f'a) Összesen {db} alkalommal húztak ki páratlan számot.\n')
# b)
db1=0
db2=0
for lotto in lottok:
    paratlanok=list(filter(lambda szam:szam%2==1,lotto))
    if len(paratlanok)>0:
        db1+=1
        db2+=len(paratlanok) # ez az a) feladat eredménye

print(f'b) {db1} héten húztak ki páratlan számot. Összesen {db2} alkalommal.')
print("\n7. feladat\n")
lottok.append(lotto52het)
kitxt = open("lotto52.ki","w")

for lotto in lottok:
    for szam in lotto:
        kitxt.write(f'{szam:2} ') # kicsit szebben
        kitxt.write("\n")

kitxt.close()

print(f'A lotto52.ki fájl kiíratása és a fájl lezárása sikeresen befejeződött.')
print("\n8. feladat\n")
##1 A gyakorisági táblázatot ki kell egészíteni az 52. hét számaival
for szam in lotto52het:
    gyak[szam-1]+=1

for i,n in enumerate(gyak):
    print(n, end=" ")
    if (i+1)%15==0:
        print()

print()

print("\n9. feladat\n")
primek=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89]
print("Egyszer sem kihúzott prímek: ",end="")
for p in primek:
    if gyak[p-1]==0:
        print(p,end=" ")
        
print("\n")
input("A befejezéshez nyomd meg az ENTER billentyűt!")