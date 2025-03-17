hazszam = [5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30]
szelesseg = [15,15,15,15,20,20,20,20,20,20,15,20,20,20,20,25,25,25,25,25,25,25,30,25,25,30,30,30,35,35,35,35]
hosszusag = [55,50,0,0,45,40,30,45,35,0,0,0,0,0,0,25,45,35,45,40,30,0,0,0,0,25,0,0,30,35,0,0]

n = len(hazszam)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if szelesseg[j] > szelesseg[j-1]:
            hazszam[j], hazszam[j-1] = hazszam[j-1], hazszam[j]
            szelesseg[j], szelesseg[j-1] = szelesseg[j-1], szelesseg[j]
            hosszusag[j], hosszusag[j-1] = hosszusag[j-1], hosszusag[j]            

for i in range(n):
    print(hazszam[i], szelesseg[i], hosszusag[i])

