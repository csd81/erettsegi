# a) feladat
ajandek = [0]*11
ajandek[0] = 6
ajandek[1] = 5
ajandek[2] = 8
ajandek[3] = 7
ajandek[4] = 10
ajandek[5] = 3
ajandek[6] = 1
ajandek[7] = 2
ajandek[8] = 0
ajandek[9] = 4
ajandek[10] = 9
# b) feladat
print("A 7. tanuló a %d. tanulónak adott ajándékot." % (ajandek[7]))
# c) feladat
print(ajandek[ajandek[7]])
# d) feladat
print("Csere előtt: 3. tanuló adott a %d.-nek, a 4. tanuló a %d.-nek" % (ajandek[3], ajandek[4]))
ajandek[3], ajandek[4] = ajandek[4], ajandek[3]
print("Csere után: 3. tanuló adott a %d.-nek, a 4. tanuló a %d.-nek" % (ajandek[3], ajandek[4]))
# e) feladat
nev = ["András", "Béla", "Cecília", "Dóra", "Elemér", "Fanni", "Glória", "Hedvig", "Ilona", "József", "Katalin"]
# f) feladat
sz = int(input("Kérek egy sorszámot (0 - 10): "))
print("%s %s-t ajándékozta meg." % (nev[sz], nev[ajandek[sz]]))
# g) feladat
ssz = int(input("Kérek egy sorszámot (0 - 10): "))
print("%s -> %s -> %s" % (nev[ssz], nev[ajandek[ssz]], nev[ajandek[ajandek[ssz]]]))
