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

print( kerekit(6238))
print( kerekit(6586))
print( kedvezmeny(1000,15,15))
print( kedvezmeny(1000,35,15))
print( kedvezmeny(1000,35,10))
print( kedvezmeny(1000,35,25))
print( ado(50,30))
print( ado(20,40))
print( ado(20,25))
