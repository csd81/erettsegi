hazszam = [5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30]
szelesseg = [15,15,15,15,20,20,20,20,20,20,15,20,20,20,20,25,25,25,25,25,25,25,30,25,25,30,30,30,35,35,35,35]
hosszusag = [55,50,0,0,45,40,30,45,35,0,0,0,0,0,0,25,45,35,45,40,30,0,0,0,0,25,0,0,30,35,0,0]

def kerekit(be):
    ki = 100 * int(be / 100)
    if be % 100 >= 50:
        ki += 100
    return ki

def kedvezmeny(a, h, sz):
    if h <= 25 or sz <= 15:
        a *= 0.8
    return a

def ado(hosszusag, szelesseg):
    terulet = hosszusag * szelesseg
    if terulet <= 700:
        fab = terulet * 51
    else:
        fab = 700 * 51
    if 1000 >= terulet > 700:
        fab += 39 * (terulet - 700)
    if terulet > 1000:
        fab += 39 * 300
        fab += 200
    return kerekit(kedvezmeny(fab,hosszusag,szelesseg))

s = 0
for i in range(len(hazszam)):
    if hazszam[i] % 2 == 1:
        s += ado(hosszusag[i],szelesseg[i])
print("%d Fabatka adóra lehet számítani a Gazdagsorról." % (s))
