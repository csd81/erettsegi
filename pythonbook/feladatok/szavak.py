print("1. feladat")
szo = input("Kérek egy szót: ")
mgh = "aeiou"
h = len(szo)
i = 0
while i <= h-1 and not(szo[i] in mgh):
    i+=1
if i > h-1:
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó.")

print("3. feladat")
be = open("szoveg.txt","r")
szo = be.readline()
szo = szo.strip()
h = len(szo)
legh = h
leghszo = szo
dbmagan = 0
db = 0
otbetus = []
while szo!="":
    db+=1
    magan,massal = 0,0
    for betu in szo:
        if betu in mgh: 
            magan+=1
    massal = h -  magan
    if magan > massal:
        dbmagan+=1
        print (szo, end=" ")
    if legh < h:
        legh, leghszo = h, szo
    if h == 5:
        otbetus.append(szo)
    szo = be.readline()
    szo = szo.strip()
    h = len(szo)
be.close()
print("\n", dbmagan, "/", db, " : ", \
      "{:.2f}" . format(100*dbmagan/db), sep="")
print("2. feladat")
print("Leghosszabb szo hossza %d, például: %s." %(legh, leghszo))
print("4. feladat")
keresettszo = input("Kérek egy 3 betűs szót: ")
print("Hozzá tartozó létraszavak: ")
for vizsgalt in otbetus:
    if vizsgalt[1:4] == keresettszo:
       print(vizsgalt, end=" ")
print("5. feladat")
i = 0
while i < len(otbetus)-2:
    j = len(otbetus)-1
    while j>i:
        if otbetus[j][1:4] < otbetus[j-1][1:4]:
            otbetus[j],otbetus[j-1] = otbetus[j-1],otbetus[j]
        j-=1
    i+=1
ki = open("letra.txt","w")
if otbetus[0][1:4] == otbetus[1][1:4]:
    ki.write(otbetus[0]+"\n")
i = 1
while i < len(otbetus)-2:
    if otbetus[i][1:4] == otbetus[i-1][1:4] or \
       otbetus[i][1:4] == otbetus[i+1][1:4]:
        ki.write(otbetus[i]+"\n")
    if otbetus[i][1:4] == otbetus[i-1][1:4] and \
       otbetus[i][1:4] != otbetus[i+1][1:4]:
        ki.write("\n")
    i+=1
veg = len(otbetus)-1
if otbetus[veg][1:4] == otbetus[veg-1][1:4]:
    ki.write(otbetus[veg]+"\n")
ki.close()















