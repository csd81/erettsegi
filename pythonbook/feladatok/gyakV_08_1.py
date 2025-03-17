from random import randrange

#a) feladat
class Sites():
    pass
site = []
for i in range(10):
    site.append(Sites())

#c) és e) feladat    
def sitesout():
    for i in range(10):
        t = site[i].wi * site[i].lo
        print("A %d. számú telek területe %d négyzetméter" % \
              (site[i].num, t))
    print()

#b) feladat
for i in range(10):
    site[i].num = i + 1
    site[i].wi = randrange(10,31)
    site[i].lo = randrange(50,101)

sitesout()

#d) feladat
for i in range(5):
    site[i], site[9-i] = site[9-i], site[i]

sitesout()
