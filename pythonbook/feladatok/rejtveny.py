def egyezotabla(atvett):
    global megoldasok, feladvany
    egyezo = 1
    i = 0
    while i < 10 and egyezo == 1:
        j = 0
        while j < 10 and egyezo == 1:
            if 10 > megoldasok[(i,j,atvett)]:
                if megoldasok[(i,j,atvett)] != feladvany[(i,j)]:
                    egyezo = 0
            j+=1
        i+=1
    return egyezo

def hajodarabjo(atvett):
    global megoldasok
    dbhajo = 0
    for i in range(10):
        for j in range(10):
            if 11 == megoldasok[(i,j,atvett)]:
                dbhajo+=1
    if dbhajo == 12:
        return 1
    else:
        return 0

def szomszedsagjo(atvett):
    global megoldasok
    jo = 1
    x = 0
    while x < 10 and jo == 1:
        y = 0
        while y < 10 and jo == 1:
            i = x - 1
            while i < x + 2 and jo == 1:
                j = y - 1
                while j < y + 2 and jo == 1:
                    if i >= 0 and i < 10 and j >= 0 and j < 10 and \
                       not(x == i and y == j):
                        if megoldasok[(x,y,atvett)] != 0 and \
                           megoldasok[(i,j,atvett)] != 0:
                            jo = 0
                    j+=1
                i+=1
            y+=1
        x+=1
    return jo

def annyitlat(atvett):
    global megoldasok
    jo = 1
    x = 0
    while x < 10 and jo == 1:
        y = 0
        while y < 10 and jo == 1:
            if 0 < megoldasok[(x,y,atvett)] < 11:
                dbv, dbf = 0,0
                for i in range(10):
                    if megoldasok[(x,i,atvett)] == 11:
                        dbf+=1
                    if megoldasok[(i,y,atvett)] == 11:
                        dbv+=1
                if dbv+dbf != megoldasok[(x,y,atvett)]:
                    jo = 0
            y+=1
        x+=1
    return jo

feladvany = {}
megoldasok = {}
megfejtok = []
print("1. feladat")
x = int(input("Kérem a torony helyének oszlopszámát: "))
y = int(input("Kérem a torony helyének sorszámát: "))
h = int(input("Kérem a toronyból látható hajók számát: "))
if h > 3:
    print("Nehéz torony.")
print("2. feladat")
i = x - 1
while i <= x + 1:
    j = y - 1
    while j <= y + 1:
        if i > 0 and i <11 and j > 0 and j < 11 and \
           not(x == i and y == j):
            print(i, j)
        j+=1
    i+=1
print("3. feladat")
be = open("feladvany.txt","r")
for i in range(10):
    line = be.readline()
    atm = line.split()
    for j in range(len(atm)):
        feladvany[(i,j)] = int(atm[j])
be.close()
be = open("megoldas.txt","r")
line = be.readline()
dbmegfejtok = int(line)
for k in range(dbmegfejtok):
    line = be.readline()
    megfejtok.append(line.strip())
    for i in range(10):
        line = be.readline()
        atm = line.split()
        for j in range(len(atm)):
            megoldasok[(i,j,k)] = int(atm[j])
be.close()
dbehet, dbhajorossz, dbszomszedrossz = 0,0,0
for k in range(dbmegfejtok):
    if hajodarabjo(k) == 0:
        dbhajorossz+=1
    if szomszedsagjo(k) == 0 and hajodarabjo(k) == 1 and \
       egyezotabla(k) == 1:
        dbszomszedrossz+=1
    if egyezotabla(k) == 0:
        dbehet+=1
        print(megfejtok[k], end=" ")
if dbehet == 0:
    print("Mindegyik megfejtés erre a hétre érkezett.")
print("\n4. feladat")
print("A hajók száma ennyi megoldáson hibás: ", dbhajorossz)
print("5. feladat")
print("A szomszédság nem megfelelő ennyi esetben: ", dbszomszedrossz)
print("6. feladat")
dbhelyes=0
for k in range(dbmegfejtok):
    if szomszedsagjo(k) == 1 and hajodarabjo(k) == 1 and \
       egyezotabla(k) == 1 and annyitlat(k)==1:
        dbhelyes+=1
        print(megfejtok[k], end=" ")
print("\nÖsszesen ennyi helyes megfejtés érkezett: ", dbhelyes)
