hazszam = [5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30]

def disp():
    for i in range(len(hazszam)):
        print(hazszam[i], end=' ')
    print()
    
disp()
n = len(hazszam)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if hazszam[j] < hazszam[j-1]:
            hazszam[j], hazszam[j-1] = hazszam[j-1], hazszam[j]
disp()
