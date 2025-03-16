"""
2006. május: Fehérje
@author Klemand66
"""

print("\n1. feladat\n")

betxt = open("aminosav.txt")

asavak=[]

for sor in betxt:
    asav=[sor.strip()]                     # 0: rövidítés
    sor = next(betxt).strip()
    asav.append(sor)                       # 1: betűjel
    sor = next(betxt).strip()
    asav.append(int(sor))                  # 2: C
    sor = next(betxt).strip()
    asav.append(int(sor))                  # 3: H
    sor = next(betxt).strip()
    asav.append(int(sor))                  # 4: O
    sor = next(betxt).strip()
    asav.append(int(sor))                  # 5: N
    sor = next(betxt).strip()
    asav.append(int(sor))                  # 6: S
    asavak.append(asav)

betxt.close()
print("A beolvasás és a fájl lezárása sikeresen befejeződött.")


print("\n2. feladat\n")

at=[12,1,16,14,32] 

"""
Egy új oszlopot illesztünk a táblázat végére.
"""

for asav in asavak:
    rmt=0
    for i in range(2,7):
        rmt+=asav[i]*at[i-2]
    asav.append(rmt)                       # 7: relatív molekulatömeg
    
print("A relatív molekulatömegek meghatározása befejeződött.")


kitxt = open("eredmeny.txt","w")

print("\n3. feladat\n")
kitxt.write("3. feladat\n")

asavak.sort(key=lambda asav:asav[7])

for asav in asavak:
    print(f'{asav[0]} {asav[7]}')
    kitxt.write(f'{asav[0]} {asav[7]}\n')

kitxt.close()
print("\nA kiíratás és a szövegfájl lezárása sikeresen befejeződött.")


betxt = open("bsa.txt")

bsa=[]
for sor in betxt:
        bsa.append(sor.strip())  

betxt.close()

kitxt = open("eredmeny.txt","a")

print("\n4. feladat\n")
kitxt.write("\n4. feladat\n")

jeloszlop=list(map(lambda i:asavak[i][1],range(len(asavak))))

elemjel=["C","H","O","N","S"]
elemdb=[0,0,0,0,0]   

for jel in bsa:
    i=jeloszlop.index(jel)
    for j in range(5):
        elemdb[j]+=asavak[i][j+2]

elemdb[1]-=2*(len(bsa)-1) # A vízmolekulák kilépésének beszámítása
elemdb[2]-=(len(bsa)-1)

print(f'A BSA nevű fehérje összegképlete: ',end="")
kitxt.write(f'A BSA nevű fehérje összegképlete: ')

for i,jel in enumerate(elemjel):
    print(f'{jel} {elemdb[i]} ',end="")
    kitxt.write(f'{jel} {elemdb[i]} ')

print()
kitxt.write("\n")

kitxt.close()
print("\nA kiíratás és a szövegfájl lezárása sikeresen befejeződött.")


print("\n5. feladat\n")

aktkezdet=None
akthossz=0
maxkezdet=None
maxhossz=0

for i,jel in enumerate(bsa):
    if aktkezdet==None:
        aktkezdet=i
    akthossz+=1                 
    if akthossz>maxhossz:       
        maxkezdet=aktkezdet     
        maxhossz=akthossz       
    if jel in "YWF": # A hasítás a megadott elemek után történik!                     
        aktkezdet=None
        akthossz=0

print("A Kimotripszin enzimmel széthasított BSA lánc leghosszabb darabja\n")
print(f'A szakasz előtti hasító aminosav a {maxkezdet}. sorszámú {bsa[maxkezdet-1]}.')
print(f'A kezdő aminosav a {maxkezdet+1}. sorszámú {bsa[maxkezdet]}, a szakasz hossza: {maxhossz},')
print(f'az utolsó, a hasító elem a {maxkezdet+maxhossz}. sorszámú {bsa[maxkezdet+maxhossz-1]}.') 


print("\n6. feladat\n")

hasitasok=list(map(lambda i : bsa[i]=="R" and (bsa[i+1]=="A" or bsa[i+1]=="V") ,range(len(bsa))))
# minden indexhez hozzárendeljük, hogy történt-e hasítás a bsa-ban az adott helyen

if True in hasitasok:
    elsohasitas=hasitasok.index(True)
    db=bsa[:elsohasitas].count("C")
    print(f'Az első hasítási láncban {db} Cisztein található.')
else:
    print("A Factor XI enzim nem hasította a BSA-láncot")
    

input("\nA befejezéshez nyomd meg az ENTER billentyűt!")
