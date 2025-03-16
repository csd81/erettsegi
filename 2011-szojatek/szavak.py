"""
2011. május: Szójáték
@author Klemand66
"""

print("\n1. feladat\n")

def mghszamlalo(szoveg):
    mghk="aeiou"
    mghlista=list(filter(lambda betu:betu in mghk,szoveg))
    return len(mghlista)
    
szo=input("Kérek egy szót, mely csak az angol abc kisbetűit tartalmazza: ")

if mghszamlalo(szo)>0:
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.")



print("\n2. feladat\n")

betxt = open("szoveg.txt")

"""
Csak beolvassuk egyenként a sorokat, és tárolás nélkül dolgozzuk fel.
Így most nem alkalmazható a max(), map(), filter() függvények egyike sem,
a klasszikus programozási tételeket kell használni.
"""

maxhossz,maxszo=0,None
for sor in betxt:
    aktszo=sor.strip()
    if len(aktszo)>maxhossz:
        maxhossz=len(aktszo)
        maxszo=aktszo 
    
betxt.close()
print(f'A leghosszabb szó: {maxszo}, hossza: {maxhossz} karakter.')



print("\n3. feladat\n")

print("A több magánhangzót tartalmazó szavak:")

betxt = open("szoveg.txt")

db,dbtobb=0,0

for sor in betxt:
    db+=1
    aktszo=sor.strip()
    if len(aktszo)<2*mghszamlalo(aktszo):
        print(aktszo,end=" ")
        dbtobb+=1
        if dbtobb%12==0:
            print()        
    
betxt.close()

print(f'\n{dbtobb}/{db} : {100*dbtobb/db:.2f}%')



print("\n4. feladat\n")

betxt = open("szoveg.txt")

szavak5=[]
for sor in betxt:
    aktszo=sor.strip()
    if len(aktszo)==5:
        szavak5.append(aktszo)      
    
betxt.close()

fok=input("Kérek egy 3 karakteres szórészletet (pl. isz vagy obo): ")

print(f'A megadott {fok} létrafok létraszavai: ')

for szo in szavak5:
    if szo[1:-1]==fok:
        print(szo,end=" ")
print()
        


print("\n5. feladat\n")

fokok,letraszolistak=[],[]
for szo in szavak5:
    aktfok=szo[1:-1]
    if aktfok in fokok:
        aktindex=fokok.index(aktfok)
        letraszolistak[aktindex].append(szo)
    else:
        fokok.append(aktfok)
        letraszolistak.append([szo]) # itt nyitjuk az új létraszólistát

kitxt = open("letra.txt","w")

for lista in letraszolistak:
    if len(lista)>1:
        for szo in lista:
            kitxt.write(f'{szo}\n')
        kitxt.write("\n")
            
kitxt.close()
print("A kiíratás és a szövegfájl lezárása sikeresen befejeződött.\n")


input("\nA befejezéshez nyomd meg az ENTER billentyűt!")

