def kmtoft(km):
    if km < 3:
        return 500
    elif km < 6:
        return 700
    elif km < 11:
        return 900
    elif km < 21:
        return 1400
    else:
        return 2000
    
nap = []
ut = []
tav = []
print("1. feladat")
i = 0
be = open("tavok.txt","r")
line = be.readline()
while line !="":
    bont = line.split()
    nap.append( int(bont[0]))
    ut.append(int(bont[1]))
    tav.append(int(bont[2]))
    line = be.readline()
be.close()
print("Fájlbeolvasás kész.")
print("2. feladat")
napmin, napmax = 10, 0
for i in nap:
    if i < napmin:
        napmin = i
    if i > napmax:
        napmax = i
utmin, utmax = 50, 0
tavmin, tavmax = 0, 0
for i in range(len(nap)):
    if ut[i] < utmin and nap[i] == napmin:
        utmin = ut[i]
        tavmin = tav[i]
    if ut[i] > utmax and nap[i] == napmax:
        utmax = ut[i]
        tavmax = tav[i]
print("A hét első útja kilométerben: ", tavmin)
print("3. feladat")
print("A hét utolsó útja kilométerben: ", tavmax)
print("4. feladat")
napifuvar = []
napitav = []
for i in range(7):
    napifuvar.append(0)
    napitav.append(0)
for i in range(len(nap)):
    napifuvar[nap[i]-1] += 1
    napitav[nap[i]-1] += tav[i]
print("Ezeken a napokon nem dolgozott a futár: ", end=" ")
for i in range(7):
    if napifuvar[i] == 0:
        print(i + 1, end = " ")
print("\n6. feladat")
legtobbfuvar = -1
legtobbfuvarnap = -1
for i in range(7):
    if napifuvar[i] > legtobbfuvar:
        legtobbfuvar = napifuvar[i]
        legtobbfuvarnap = i
    print(i+1, ".nap: ", napitav[i], " km", sep="")
print("5. feladat")
print("A legtöbb fuvar ezen a napon volt: ", legtobbfuvarnap+1)
print("7. feladat")
t = int(input("Kérek egy távolságot: "))
print("Ennyi díjazás jár érte Ft-ban: ", kmtoft(t))
i = 0
while i < len(nap)-2:
    j = len(nap)-1
    while j > i:
        if 1000*nap[j]+ut[j] < 1000*nap[j-1]+ut[j-1]:
            nap[j], nap[j-1] = nap[j-1], nap[j]
            ut[j], ut[j-1] = ut[j-1], ut[j]
            tav[j], tav[j-1] = tav[j-1], tav[j]
        j-=1
    i+=1
osszeg = 0
ki=open("dijazas.txt","w")
for i in range(len(nap)):
    ki.write(str(nap[i])+".nap "+str(ut[i])+ \
        ".út: "+str(kmtoft(tav[i]))+" Ft\n")
    osszeg+=kmtoft(tav[i])
ki.close()
print("A kiírás a dijazas.txt fájlba befejeződött")
print("9. feladat")
print("A kifizetett összeg: ",osszeg," Ft", sep="")
    
